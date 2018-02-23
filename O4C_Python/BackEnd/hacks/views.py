import itertools
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework import viewsets
from corsheaders.signals import check_request_enabled
from hacks.models import Pilot, Event, EventParticipation, WorkGroups#, Facilitator
from .serializers import DetailsPilotSerializer, DetailsEventSerializer, PaticipationEventStatusSerializer, GroupSerializer#, FacilitatorSerializer
from tools.models import Hackproces, Projects, ProjectFiles
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

class PiloList(APIView):
    # Only Authenticated users has access
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        pilots = Pilot.objects.all()
        serializer = DetailsPilotSerializer(pilots, many=True)
        return Response(serializer.data)

class TTQ(APIView):
    def __init__(self):
            print ("in init")
    
    def delete(self, request, Gid):
        group = WorkGroups.objects.get(id=Gid)
        group.users.clear()
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    def post(self, request, Gid):
        group = WorkGroups.objects.get(id = Gid)
        group.name = request.data['name']
        group.save()
        return Response('Group updated !')

    def get(self, request, Gid):
        group = WorkGroups.objects.get(id = Gid)
        return Response(group.name)


class GroupsList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        groups = WorkGroups.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        fonction = request.data['fonc']
        response = any

        if fonction == '1':
               response = self.fetch_groups_of_event(request.data)
        elif fonction == '2':
            response = self.assign_to_group(request.data)
        elif fonction == '3':
            response = self.unassign_to_group(request.data)
        elif fonction == '4':
            response = self.group_new(request.data)
        elif fonction == '5':
            response = self.validate_group(request.data)
        elif fonction == '6':
            response = self.fetch_user_group(request)
        elif fonction == '7':
            response = self.fetch_allgroups_of_event(request.data)
        elif fonction == '8':
            response = self.verify_group_event(request)
        return Response(response)

    def fetch_groups_of_event(self, request):
        goups = WorkGroups.objects.filter(event_id=request['event'])
        serializer = GroupSerializer(goups, many=True)
        return serializer.data

    def assign_to_group(self, request):
        record = WorkGroups.objects.get(id=request['group'])
        record_user = User.objects.get(id=request['user'])
        msg = 'Should be done !'
        if (record.users.add(record_user)): 
            msg = 'Error'
        return msg

    def unassign_to_group(self, request):
        record = User.objects.get(id=request['user'])
        groups = WorkGroups.objects.get(users__id__contains=record.id, event_id=request['event'] )
        groups.users.remove(record)
        msg = 'Should be done !'
        return msg

    def group_new(self, request):
        event = Event.objects.get(id=request['event_id'])
        newGroup = WorkGroups(name=request['name'], event=event, status=0)
        newGroup.save()
        return 'New group created !'

    def validate_group(self, request):
        group = WorkGroups.objects.get(id=request['group'])
        group.status = 1
        group.save()
        return 'Group validated'

    def fetch_user_group(self, request):
        user = User.objects.get(id=request.user.id)
        event = Event.objects.get(id=request.data['event'])
        record = WorkGroups.objects.get(event=event, users=user)
        serlizer = GroupSerializer(record)
        return serlizer.data

    def fetch_allgroups_of_event(self, request):
        goups = WorkGroups.objects.filter(event_id=request['event'])
        serializer = GroupSerializer(goups, many=True)
        return serializer.data

    def verify_group_event(self, request):
        try:
            group = WorkGroups.objects.get(users=request.user.id, event=request.data['event'])
            return group.status
        except WorkGroups.DoesNotExist:
            return 'Null'

class EventManage(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, ev_id):
        event = Event.objects.get(id=ev_id)
        serialized = DetailsEventSerializer(event)
        return Response(serialized.data)

    def post(self, request, ev_id):
        event = Event.objects.get(id=ev_id)
        event.title = request.data['title']
        event.date_start = request.data['date_start']
        event.date_end = request.data['date_end']
        event.descreption = request.data['descreption']
        event.theme = request.data['theme']
        event.save()
        return Response('Object updated')

    def delete(self, request, ev_id):
        event = Event.objects.get(id = ev_id)
        groups = WorkGroups.objects.filter(event=event)
        if(len(groups)>0):
            for item in groups:
                item.users.remove()
                try: 
                    project = Projects.objects.get(group=item)
                    project.files.remove()
                    project.delete()
                except:
                    pass
                item.delete()
        try:
            process = Hackproces.objects.get(for_event=event)
            process.outil_used.remove()
            process.delete()
        except:
            pass
        event.delete()
        return Response('Delete completed')
        

class EventList(APIView):
    # Only Authenticated users has access
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        resp = None;
        listPilot = Pilot.objects.filter(user=request.user.id).values_list('id', flat=True)
        for item in listPilot:
            events = Event.objects.filter(hackathon_id=item)
            resp = DetailsEventSerializer(events, many=True)
        return Response(resp.data)

    def post(self, request):
        fonction = request.data['fonc']
        response = any
        if fonction == '0':
            response = self.event_applied()
        elif fonction == '1':
            response = self.upcoming_events(request.data)
        elif fonction == '2':
            response = self.subscribtion_status(request.data)
        elif fonction == '3':
            response = self.user_per_event(request.data)
        elif fonction == '4':
            response = self.addEvent(request)
        return Response(response)

    def addEvent(self, request):
        Sdate = request.data['Sdate'].replace('"', '')
        Edate = request.data['Edate'].replace('"', '')
        pilotid = request.data['pilotid'].replace('"', '')
        timezone.deactivate()
        pilot = Pilot.objects.get(id=pilotid)
        newEvent = Event(hackathon= pilot, title=request.data['title'],  theme=request.data['theme'], descreption=request.data['descreption'], date_start=Sdate, date_end=Edate, image = request.FILES['path'])
        srcA = newEvent.save()
        return 'sucess'

        
    def event_applied(self):
        record = EventParticipation.objects.filter(status='pending').order_by('event_id').values_list('event_id', flat=True).distinct()
        my_list = []
        for line in record:
            event = Event.objects.filter(id=line).values('id','title', 'theme', 'date_start')
            my_list.extend(event)
        return my_list

    def user_per_event(self, request):
        part = EventParticipation.objects.select_related('participant').filter(event_id=request['event'], status='pending')
        mylista = []
        for ele_part in part:
            data = {'id': ele_part.participant.id, 'mail': ele_part.participant.email, 'actived': ele_part.participant.is_active, 'name': ele_part.participant.first_name+' '+ele_part.participant.last_name
                }
            mylista.append(data)
        return mylista;

    def subscribtion_status(self, request):
        try: 
            upcoming = EventParticipation.objects.get(participant_id=request['participant'], event_id=request['event'])
            return upcoming.status
        except :
            return 'none'
    
    def upcoming_events(self, request):
        events = any
        lista = []
        eventWithProcess = Hackproces.objects.all().values_list('for_event_id', flat=True) 
        for item in eventWithProcess:
            event = Event.objects.get(id=item)
            lista.append(event)
        subscribed = EventParticipation.objects.filter(participant_id=request['id']).values_list('event_id', flat=True)
        for item in subscribed:
            for objet in lista:
                if(objet.id==item):
                        lista.remove(objet)
        serializer = DetailsEventSerializer(lista, many=True)
        return serializer.data
    
    def applied_for_event(self, request):
        record = Event.objects.distinct('event_id')
        query= record.hackathon_set.all()
        return query

class GroupsCount(APIView):
    def get(self, request):
        listA= []
        hackID = Pilot.objects.filter(user=request.user.id).values_list('id', flat=True)
        events = Event.objects.filter(hackathon_id=hackID)
        for item in events:
            listB = []
            count = WorkGroups.objects.filter(event_id=item.id).count()
            listB.append({'event':item.id, 'group': count})
            listA.extend(listB)
        return Response(listA)

class EventOrganization(APIView):

    def get(self, request):
        record = Pilot.objects.filter(user=request.user.id).values_list('user__id','id')
        #ser = DetailsPilotSerializer(record, many=True)
        return Response(record)

    def post(self, request):
        fonction = request.data['fonc']
        response = any

        if fonction == '1':
           response = self.eventlist(request)
        elif fonction == '2':
           response = self.subscribeToevent(request.data)
        elif fonction == '3':
           response = self.acceptApplicant(request.data)
        elif fonction == '4':
            response = self.refusApplicant(request.data)
        return Response(response)

    def acceptApplicant(self, request):
        event = Event.objects.get(id=request['eventID'])
        even_title = event.title
        record = EventParticipation.objects.get(participant_id=request['userId'], event_id=request['eventID'])
        record.status= 'confirmed'
        record.save()
        inputs = {'status':1, 'recepiant':request['mail'], 'title':even_title}
        self.sendNotif(inputs)
        return 'success'

    def refusApplicant(self, request):
        event = Event.objects.get(id=request['eventID'])
        even_title = event.title
        record = EventParticipation.objects.get(participant_id=request['userId'], event_id=request['eventID'])
        record.status= 'rejected'
        record.save()
        inputs = {'status':0, 'recepiant':request['mail'], 'title':even_title}
        self.sendNotif(inputs)
        return 'success'

    def eventlist(self, request):
        hacks = EventParticipation.objects.filter(participant_id=request.data['id']).values('event_id', 'event__title', 'event__date_start', 'event__date_end', 'event__hackathon_id', 'status', 'event__image').order_by('-event__date_start')
        return hacks

    #This function is not recomnded --> need to be changed in the future for security reason
    def subscribeToevent(self, request):
        eventlink = Event.objects.get(id=request['eventid'])
        userlink = User.objects.get(id=request['participantid'])
        subscribtion = EventParticipation(event=eventlink, participant=userlink, status=request['status'])
        subscribtion.save()
        res = 'success'
        return res

    def sendNotif(self, request):
        mail = request['recepiant']
        situation = request['status']
        notif = any
        if situation == 0:
            notif = ' unfortunately the numbers of applicant is atteint so you request has been rejected.'
        else :
            notif = ' your request has been accepted. Please be at the venue in time.'
        if(send_mail(
                'About your request to attend '+request['title'],
                'Thank you for your interest and request to attend,'+notif,
                settings.EMAIL_HOST_USER,
                [mail],
                fail_silently=False
        )):
            return '200'
        return '350'