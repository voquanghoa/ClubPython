

from django.db import models
from django.contrib import admin
from django.utils.datetime_safe import datetime
from rest_framework import serializers


class Event(models.Model):
    title = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=2048)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    place = models.CharField(max_length=2048, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()


class EventForm(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'place', 'latitude', 'longitude']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'place', 'latitude', 'longitude']
