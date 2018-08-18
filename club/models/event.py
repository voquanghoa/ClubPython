from django.db import models
from django.contrib import admin


class Event(models.Model):
    description = models.CharField(max_length=2048)
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()


class EventForm(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ['description', 'created_time', 'update_time']