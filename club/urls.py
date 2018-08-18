from django.conf.urls import include, url

from club.controllers import events

urlpatterns = [
    url(r'', events.events),
]