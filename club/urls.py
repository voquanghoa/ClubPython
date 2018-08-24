from django.conf.urls import url

from club.views.dashboards import Dashboards
from club.views.event_actions import EventAction
from club.views.events import EventView, EventList, EventPost
from club.views.moneys import MoneyView, MoneyList
from club.views.outcomes import OutcomeView, OutcomeList
from club.views.users import UserList, MeDetail

urlpatterns = [
    url(r'/events$', EventPost.as_view()),
    url(r'/events(?:/(?P<event_type>(all|new|going|past)))$', EventList.as_view()),
    url(r'/events/action', EventAction.as_view()),
    url(r'/events/(?P<pk>[0-9]+)$', EventView.as_view()),

    url(r'/moneys$', MoneyList.as_view()),
    url(r'/moneys/(?P<pk>[0-9]+)$', MoneyView.as_view()),

    url(r'/users$', UserList.as_view()),
    url(r'/users/me$', MeDetail.as_view()),

    url(r'/outcomes$', OutcomeList.as_view()),
    url(r'/outcomes/(?P<pk>[0-9]+)$', OutcomeView.as_view()),

    url(r'/dashboard$', Dashboards.as_view()),
]