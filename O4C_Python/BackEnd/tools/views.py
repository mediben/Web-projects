from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import render
from .models import Outil, Hackproces, FlipCards, Projects, ProjectFiles
from hacks.models import WorkGroups, Event
from .serializers import OutilSerializer, HackprocesSerializer, FlipCardSerializer, ProjectSerializer
from rest_framework.views import status, APIView, Response
from corsheaders.signals import check_request_enabled
from django.contrib.auth.models import User
from datas.models import Tag

class OutilList(APIView):
    def get(self, request):
        outilss = Outil.objects.all()
        serializer = OutilSerializer(outilss, many=True)
        return Response(serializer.data)

class OutilSelected(APIView):
    def get(self, request, outil_id):
        spesific = Outil.objects.filter(id=outil_id)
        serializer = OutilSerializer(spesific, many=True)
        return Response(serializer.data)
        
class HackProcesList(APIView):
    def get(self, request):
        hackprocess = Hackproces.objects.all()
        serializer = HackprocesSerializer(hackprocess, many=True)
        return Response(serializer.data)

    def post(self, request):
        #request.data['lng'] = request.data['lng'].replace('"', '')
        #lng = Tag.objects.get(id=request.data['lng'])
        #print('Event '+str(request.data['tools']))
        event = Event.objects.get(id=request.data['event'])
        
        
        Eventprocess = Hackproces(for_event=event)
        Eventprocess.save()

        my_list = []
        for item in request.data['tools']:
            tool = Outil.objects.get(id=item)
            #my_list.extend(tool)
            Eventprocess.outil_used.add(tool)

        Eventprocess.save()
        return Response('success')

class HackProcesSelected(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, proces_id):
        spesific = Hackproces.objects.filter(for_event=proces_id)
        serializer = HackprocesSerializer(spesific, many=True)
        my_list = []
        if(len(serializer.data)>0):
            record = (serializer.data[0]['outil_used'])
            for tool_id in record : 
                tool = Outil.objects.filter(id=tool_id).values('id','name', 'categorys')
                my_list.extend(tool)
        return Response(my_list)

    def delete(self, request, proces_id):
        process =  Hackproces.objects.get(for_event=proces_id)
        process.outil_used.remove();
        process.delete()
        return Response('Success');

#searsh query 
class SelectedToolsForEvent(APIView):
    def get(self, request, event_id):
        spesific = Hackproces.objects.filter(for_event=event_id)
        serializer = HackprocesSerializer(spesific, many=True)
        return Response(serializer.data)

class FlipcardManger(APIView):
    #Provoque une erreur ?!!
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def get(self, request, category):
        record = FlipCards.objects.filter(typecard=category, user_id=request.user.id)
        ser = FlipCardSerializer(record, many=True)
        return Response(ser.data)

    def post(self, request):
        fonction = request.data['fonc']
        response = any
        if fonction == '0':
            response = self.addcard(request)
        elif fonction == '1':
            response = self.editcard(request)
        elif fonction == '2':
            response = self.deletecard(request.data)
        elif fonction == '3':
                response = self.fetchcard(request.data)
        return Response(response)

    def addcard(self, request):
        request.data['userID'] = request.data['userID'].replace('"', '')
        request.data['lng'] = request.data['lng'].replace('"', '')
        user = User.objects.get(id=request.data['userID'])
        lng = Tag.objects.get(id=request.data['lng'])
        fileLNK: any
        try:
            fileLNK = request.FILES['path']
        except :
            fileLNK = ''
        newCard = FlipCards(typecard=request.data['type'], title=request.data['title'], description=request.data['desc'], link=request.data['link'], path=fileLNK, user=user)
        newCard.save()
        newCard.language.add(lng)
        newCard.save()
        return 'Success'

    def editcard(self, request):
        record = FlipCards.objects.get(id=request.data['id'])
        record.title = request.data['title']
        record.link = request.data['link']
        record.description = request.data['desc']
        if(len(request.data)>5):
            record.path = request.FILES['path']
        record.save()
        return 'Success'

    def deletecard(self, data):
        record = FlipCards.objects.get(id=data['id'])
        record.delete()
        return 'Success'

    def fetchcard(self, data):
        record = FlipCards.objects.filter(typecard=data['cardtype'])
        ser = FlipCardSerializer(record, many=True)
        return ser.data

class MyProjects(APIView):
    def get(self, request):
        query = WorkGroups.objects.filter(users=request.user.id).values('event_id')
        projectslist = []
        for item in query:
            try:
                project = Projects.objects.filter(id=item['event_id']).values('id','title','created','version')
                projectslist.extend(project)
            except Exception:
                pass
        #projects = ProjectSerializer(projectslist, many=True)
        return Response(projectslist)
            
    def post(self, request):
        pass


class ProjectManagers(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, event_ID):
        event = Event.objects.get(id=event_ID)
        thegroup = WorkGroups.objects.get(users=request.user.id, event=event)
        project = Projects.objects.get(group=thegroup)
        projectserialized = ProjectSerializer(project)
        return Response(projectserialized.data)

    def post(self, request):
        fonction = request.data['fonc']
        response = any
        if fonction == '0':
            response = self.defaultaddproject(request)
        if fonction == '1':
            response = self.addprojectfiles(request)
        elif fonction == '2':
            response = self.editproject(request)
        elif fonction == '3':
            response = self.allproject(request.data)
        elif fonction == '4':
            response = self.forceupdate(request)
        elif fonction == '5':
            response = self.deleteprojectfile(request)
        return Response(response)

    def defaultaddproject(self, request):
        group = WorkGroups.objects.get(id=request.data['group'])
        newProject = Projects(title=group.name+' project', version='0.1', group= group)
        newProject.save()
        return 'Success'

    def addprojectfiles(self, request):
        #print('=====>>> '+request.data['thumbnail'])
        project = Projects.objects.get(id=request.data['id'])
        #print(project)
        filelist = request.FILES.getlist('files[]')
        i = 0
        if request.data['thumbnail'].lower() == 'true':
            thumbfile = ProjectFiles(thumbnail = True, public = True)
            projectfiles = project.files.all()
            newfile = True

            u = 0
            while u < len(projectfiles):
                #print('=====>>> ' + projectfiles[u].thumbnail)
                if projectfiles[u].thumbnail.lower() == 'true':
                    thumbfile = projectfiles[u]
                    newfile = False
                u += 1

            thumbfile.path = filelist[i] 
            thumbfile.fileformat = filelist[i].name.split('.')[1]
            thumbfile.save()

            if newfile:
                project.files.add(thumbfile)
        else:
            while i < len(filelist):
                newprojectfile = ProjectFiles(path = filelist[i], fileformat = filelist[i].name.split('.')[1], thumbnail = False, public = request.data['public'].lower() == 'true')
                newprojectfile.save()

                project.files.add(newprojectfile)
                print(filelist[i])
                i += 1

        return 'success'

    def editproject(self, request):
        project = Projects.objects.get(id=request.data['id'])
        #print('=====>>> ' + str(type(project.version)))
        #print('=====>>> ' + project.version)

        dbversion = project.version.split('.')
        editversion = request.data['version'].split('.')
        versionbool = ((int(editversion[0]) > int(dbversion[0])) or (int(editversion[0]) == int(dbversion[0]) and int(editversion[1]) >= int(dbversion[1])))

        if versionbool:
            data = request.data
            project.title = data['title']
            project.corevalue = data['corevalue']
            project.datasource = data['datasource']
            project.contactinfo = data['contactinfo']
            project.version = (dbversion[0] + "." + str(int(dbversion[1]) + 1))
            #print('=====>>> ' + dbversion[0] + "." + dbversion[1] + " >> " + project.version)
            project.save()
            return 'success'
        else:
            return 'outdated'

    def allproject(self, request): 
        projects = Projects.objects.all()
        serialized = ProjectSerializer(projects, many=True)
        return serialized.data

    def forceupdate(self, request):
        project = Projects.objects.get(id=request.data['id'])  
        dbversion = project.version.split('.')
        data = request.data
        project.title = data['title']
        project.corevalue = data['corevalue']
        project.datasource = data['datasource']
        project.contactinfo = data['contactinfo']
        project.version = (dbversion[0] + "." + str(int(dbversion[1]) + 1))
        #print('=====>>> ' + dbversion[0] + "." + dbversion[1] + " >> " + project.version)
        project.save() 
        return 'success'
    
    def deleteprojectfile(self, request):
        print('=====>>> '+request.data['id'])
        projectfile = ProjectFiles.objects.get(id=request.data['id'])  
        projectfile.delete()

        return 'success'