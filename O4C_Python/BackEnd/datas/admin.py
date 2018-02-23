from django.contrib import admin
from .models import Tag, Datasets , Participant
# Register your models here.

admin.site.register(Datasets)
admin.site.register(Tag)
admin.site.register(Participant)