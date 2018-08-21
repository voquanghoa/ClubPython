from django.conf.urls import url

from club.views.event_actions import EventAction
from club.views.events import EventView, EventList, EventPost
from club.views.moneys import MoneyView, MoneyList
from club.views.users import UserList, UserDetail

urlpatterns = [
    url(r'/events$', EventPost.as_view()),
    url(r'/events(?:/(?P<event_type>(all|new|going|past)))$', EventList.as_view()),
    url(r'/events/action', EventAction.as_view()),
    url(r'/events/(?P<pk>[0-9]+)$', EventView.as_view()),

    url(r'/moneys$', MoneyList.as_view()),
    url(r'/moneys/(?P<pk>[0-9]+)$', MoneyView.as_view()),

    url(r'/users$', UserList.as_view()),
    url(r'/users/(?P<pk>[0-9]+)$', UserDetail.as_view()),


]