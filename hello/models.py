from django.db import models

class Event(models.Model):
    description = models.CharField(max_length=2048)
    created_time = models.DateField()
    update_time = models.DateField()