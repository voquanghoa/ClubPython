from django.db import models
from django.contrib import admin
from django.utils.datetime_safe import datetime
from rest_framework import serializers

from club.models.user import Profile


class Event(models.Model):
    title = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=2048)

    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)

    place = models.CharField(max_length=2048, default='')
    latitude = models.FloatField(default=0)

    longitude = models.FloatField(default=0)
    created_time = models.DateTimeField()

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
            'start_time': self.start_time,
            'end_time': self.end_time,
            'place': self.place,
            'latitude': self.latitude,
            'longitude': self.longitude
        }


class EventForm(admin.ModelAdmin):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'place', 'latitude', 'longitude']


class EventSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField('get_all_users')

    def create(self, validated_data):
        event = Event(**validated_data)
        event.created_time = datetime.now()
        event.save()

        return event

    def update(self, instance, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']

        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)

        instance.place = validated_data.get('place', instance.place)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)

        instance.save()

        return instance

    def get_all_users(self, obj):
        return obj.all_users

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'start_time', 'end_time', 'place', 'latitude', 'longitude', 'users']
