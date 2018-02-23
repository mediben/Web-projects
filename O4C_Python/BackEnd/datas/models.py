from django.db import models
from hacks import models as models_hack
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
import uuid
from rest_framework.authtoken.models import Token

# Create your models here.

def scramble_file_name(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ForeignKey(Category, null=True)#,on_delete=models.CASCADE)
    def __str__(self):
           return self.name

class Datasets(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    path = models.FileField(verbose_name="File ")
    forma = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tag)
    uploaduser = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaddate = models.DateField(default=date.today, blank=True)
    external = models.BooleanField()

    def __str__(self):
        return self.name
    
class Suggestion(models.Model):
    description = models.CharField(max_length=1500)
    provider = models.CharField(max_length=500)
    usage = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.CharField(default='False', max_length=5)

    def __str__(self):
        return self.description

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=250)
    date_birth = models.DateField(default=date.today, blank=True)
    imgpath = models.ImageField(verbose_name='Avatar', default='user_avatar.png', upload_to=scramble_file_name)
    #subscribedto = models.ManyToManyField(models_hack.Event)
    #subscribedto = models.ForeignKey(hackmodels.Outil, on_delete=models.CASCADE, null=True)
    #birth_date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    def __str__(self):
           return self.profession

@receiver(post_save, sender=User)
def create_user_participant(sender, instance, created, **kwargs):
    if created:
        Participant.objects.create(user=instance)
        #for user in User.objects.all():
        #    Token.objects.get_or_create(user=user)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_participant(sender, instance, **kwargs):
    instance.participant.save()
    