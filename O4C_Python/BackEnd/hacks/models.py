from django.db import models
#from datas import models as dataset_models
from django.contrib.auth.models import User

class Pilot(models.Model):
    user = models.ManyToManyField(User)
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=500)

    def __str__(self):
       return self.city + ' ('+self.country +')'
    
class Event(models.Model):
     hackathon = models.ForeignKey(Pilot, on_delete=models.CASCADE)
     title = models.CharField(max_length=250)
     date_start = models.DateField(auto_now=False)
     date_end = models.DateField(auto_now=False)
     descreption = models.TextField();
     image = models.FileField(verbose_name='File name ');
     theme = models.CharField(max_length=350)  
     #datasets = models.ManyToManyField(dataset_models.Dataset)
     
     def __str__(self):
         return self.title+ ' - ' +self.theme
     class Meta:
        ordering = ('date_start',)    

"""
class Facilitator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pilot = models.ManyToManyField(Pilot)
    """

class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    participant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=250)
    class Meta:
        ordering = ('participant',)

class WorkGroups(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField(verbose_name='Valid')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name