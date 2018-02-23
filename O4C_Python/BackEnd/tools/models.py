from django.db import models
from datetime import date
from django.forms import widgets
from hacks import models as hack_models
from datas import models as data_models
from django.contrib.auth.models import User

class Outil(models.Model):

    categorys = models.CharField(max_length=10, default='learn', help_text='Please select the correct category of tool', verbose_name='Category ')
    name = models.CharField(max_length=150, verbose_name='Tool name ')
    description = models.TextField();
    class Meta:
        verbose_name_plural = 'Tools'

    def __str__(self):
       return self.name

class Hackproces(models.Model):
    outil_used = models.ManyToManyField(Outil)
    for_event = models.ForeignKey(hack_models.Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.for_event.title +', tools'


class FlipCards(models.Model):
    typecard = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()
    path = models.FileField(verbose_name='image')
    language = models.ManyToManyField(data_models.Tag)
    user = models.ForeignKey(User)

    def __str__(self):
           return self.title


class ProjectFiles(models.Model):
    path = models.FileField(verbose_name='image')
    fileformat = models.CharField(max_length=55)
    thumbnail = models.CharField(max_length=5)
    public = models.CharField(default='False', max_length=12)

    def __str__(self):
        return self.fileformat


class Projects(models.Model):
    title = models.CharField(max_length=255)
    version = models.CharField(max_length=10)
    corevalue = models.TextField()
    datasource = models.TextField()
    datasource = models.TextField()
    contactinfo = models.TextField()
    created = models.DateField(default=date.today, blank=False)
    defenition = models.TextField()
    files = models.ManyToManyField(ProjectFiles)
    group = models.ForeignKey(hack_models.WorkGroups)

    def __str__(self):
           return self.title
    
    class Meta:
        ordering = ('created',)   