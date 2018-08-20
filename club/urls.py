from django.conf.urls import url

from club.views.events import EventView, EventList
from club.views.moneys import MoneyView, MoneyList
from club.views.users import UserList, UserDetail

urlpatterns = [
    url(r'/events$', EventList.as_view()),
    url(r'/events/(?P<pk>[0-9]+)$', EventView.as_view()),

    url(r'/moneys$', MoneyList.as_view()),
    url(r'/moneys/(?P<pk>[0-9]+)$', MoneyView.as_view()),

    url(r'/users$', UserList.as_view()),
    url(r'/users/(?P<pk>[0-9]+)$', UserDetail.as_view())
]