from rest_framework import serializers
from .models import Tag, Participant, Category, Suggestion, Datasets
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DetailsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1

class NUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class DetailsDatasetSerializer(serializers.ModelSerializer):
    usrs = NUser(source='uploaduser')
    
    class Meta:
        model = Datasets
        fields = ('id','name','description','path','forma','uploaddate','external','tags','usrs')
        depth = 1

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'
        depth = 1

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'

class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'



