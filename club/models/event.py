from django.db import models
from django.contrib import admin
from django.utils.datetime_safe import datetime
from rest_framework import serializers

from club.models.user import Profile


class Event(models.Model):
    title = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=2048)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    place = models.CharField(max_length=2048, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()

    users = models.ManyToManyField(Profile)

    events = models.Manager()

    def __str__(self):
        return 'Event: {} {} {}'.format(self.id, self.title, self.description)

    @property
    def all_users(self):
        return [profile.simple() for profile in self.users.all()]

    def sample(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date_time': self.date_time,
            'place': self.place,
            'latitude': self.latitude,
            'longitude': self.longitude
        }


class EventForm(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'place', 'latitude', 'longitude']


class EventSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField('get_all_users')

    def create(self, validated_data):
        event = Event(**validated_data)
        event.created_time = datetime.now()
        event.update_time = datetime.now()
        event.save()
        return event

    def update(self, instance, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.place = validated_data.get('place', instance.place)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)

        instance.update_time = datetime.now()
        instance.save()

        return instance

    def get_all_users(self, obj):
        return obj.all_users

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'place', 'latitude', 'longitude', 'users']
