from django.conf.urls import url

from club.views.events import EventView


urlpatterns = [
    url(r'/events', EventView.as_view()),
]