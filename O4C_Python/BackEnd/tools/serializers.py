
from rest_framework import serializers
from .models import Outil , Hackproces, FlipCards, Projects


class OutilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outil
        fields = '__all__'
    

class HackprocesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackproces
        fields = '__all__'

class FlipCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlipCards
        fields = '__all__'
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        depth = 1
