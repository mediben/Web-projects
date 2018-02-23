
from rest_framework import serializers
from .models import Pilot, Event, EventParticipation, WorkGroups#, Facilitator
from django.contrib.auth.models import User

class DetailsPilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'

class DetailsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class PaticipationEventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipation
        fields = '__all__'
"""
class FacilitatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilitator
        fields = '__all__'
        depth = 1
        """

class GroupSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)
     
    class Meta:
        model = WorkGroups
        fields = ('id','name', 'users', 'status')
        #depth = 1