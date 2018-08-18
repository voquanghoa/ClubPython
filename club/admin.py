from django.contrib import admin

from club.models.event import Event, EventForm

admin.site.register(Event, EventForm)
