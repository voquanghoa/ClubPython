from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.utils.datetime_safe import datetime
from rest_framework import serializers


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(default='', blank=True)

    avatar = models.TextField(max_length=1024, default='', blank=True)
    latitude = models.FloatField(default=0, blank=True)
    longitude = models.FloatField(default=0, blank=True)

    location_time = models.DateTimeField(blank=True, default=datetime.now)

    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.username

    @property
    def is_admin(self):
        return self.user.is_superuser

    def simple(self):
        return {
            'id': self.id,
            'username': self.username,
            'name':self.name,
            'avatar':self.avatar
        }

    def __str__(self):
        return '{} {} {}'.format(self.id, self.user.username, self.name)


class ProfileForm(admin.ModelAdmin):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'avatar', 'latitude', 'longitude', 'location_time']


class ProfileSerializer(serializers.ModelSerializer):

    def validate(self, data):
        username = self.initial_data.get('username')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username {0} has been taken".format(username))

        return data

    def create(self, validated_data):
        profile = Profile()
        profile.user = User()

        profile.user.set_password(self.initial_data.get('password'))
        profile.user.email = self.initial_data.get('email')
        profile.user.username = self.initial_data.get('username')
        profile.user.is_active = True

        profile.name = validated_data.get('name')
        profile.avatar = validated_data.get('avatar', '')
        profile.latitude = validated_data.get('latitude', 0)
        profile.longitude = validated_data.get('longitude', 0)

        profile.user.save()
        profile.user_id = profile.user.id

        if profile.latitude > 0 or profile.longitude > 0:
            profile.location_time = datetime.now()

        profile.save()

        return profile

    def update(self, instance, validated_data):

        instance.user = User.objects.get(pk=instance.user.pk)

        instance.avatar = validated_data.get('avatar', instance.avatar)

        latitude = validated_data.get('latitude', 0)
        longitude = validated_data.get('longitude', 0)

        if latitude > 0 or longitude > 0:
            instance.latitude = latitude
            instance.longitude = longitude
            instance.location_time = datetime.now()

        instance.save()

        return instance

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'is_admin', 'avatar', 'latitude', 'longitude', 'location_time', 'username']
