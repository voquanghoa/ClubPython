from django.db import models
from django.contrib import admin
from django.utils.datetime_safe import datetime

from rest_framework import serializers


class Outcome(models.Model):
    title = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=2048)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    amount = models.IntegerField(blank=True, default=0)

    outcomes = models.Manager()

    def __str__(self):
        return 'Outcome: {} {} {}'.format(self.id, self.title, self.amount)


class OutcomeForm(admin.ModelAdmin):
    class Meta:
        model = Outcome
        fields = '__all__'


class OutcomeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        outcome = Outcome(**validated_data)
        outcome.save()
        return outcome

    def update(self, instance, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.amount = validated_data.get('amount', instance.amount)

        instance.save()

        return instance

    class Meta:
        model = Outcome
        fields = ['id', 'title', 'description', 'date_time', 'amount']