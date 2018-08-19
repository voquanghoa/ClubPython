from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Event(models.Model):
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()
    description = models.CharField(max_length=2048)


class EventForm(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ['description', 'created_time', 'update_time']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "description"]
