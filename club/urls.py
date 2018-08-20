from django.conf.urls import url

from club.views.events import EventView, EventList

urlpatterns = [
    url(r'/events$', EventList.as_view()),
    url(r'/events/(?P<pk>[0-9]+)$', EventView.as_view()),
]