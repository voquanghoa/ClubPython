from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(default='', blank=True)

    avatar = models.TextField(max_length=1024, default='', blank=True)
    latitude = models.FloatField(default=0, blank=True)
    longitude = models.FloatField(default=0, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @property
    def email(self):
        return self.user.email

    @property
    def is_admin(self):
        return self.user.is_superuser

    def simple(self):
        return {
            'id': self.id,
            'name':self.name,
            'avatar':self.avatar
        }

    def __str__(self):
        return '{} {} {}'.format(self.id, self.user.username, self.name)


class ProfileForm(admin.ModelAdmin):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'avatar', 'latitude', 'longitude']


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        profile = Profile()
        profile.user = User()

        profile.user.password = validated_data.get('password')
        profile.user.email = validated_data.get('email')
        profile.user.username = validated_data.get('email')
        profile.user.is_active = True
        profile.name = validated_data.get('name')
        profile.avatar = validated_data.get('avatar', '')
        profile.latitude = validated_data.get('latitude', 0)
        profile.longitude = validated_data.get('longitude', 0)

        profile.save()

        return profile

    def update(self, instance, validated_data):

        instance.user = User.objects.get(pk=instance.user.pk)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()

        return instance

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'is_admin', 'avatar', 'latitude', 'longitude']
