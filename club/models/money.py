from django.db import models
from django.contrib import admin
from rest_framework import serializers


class Money(models.Model):
    title = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=2048, default='')
    amount = models.IntegerField(default=0)
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Money: {} {} {}'.format(self.id, self.title, self.description)


class MoneyForm(admin.ModelAdmin):
    class Meta:
        model = Money
        fields = ['title', 'description', 'amount', 'time']


class MoneySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        money = Money(**validated_data)
        money.save()
        return money

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.time = validated_data.get('time', instance.time)

        instance.save()

        return instance

    class Meta:
        model = Money
        fields = ['id', 'title', 'description', 'amount', 'time']