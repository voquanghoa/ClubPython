import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from club.decorators.require_super_user import has_profile
from club.models.dashboar import Dashboard
from club.models.event import Event
from club.models.money import Money


class Dashboards(APIView):

    @has_profile
    def get(self, request):
        profile = request.profile

        events = Event.events.filter(date_time__gte=datetime.date.today())

        going = events.filter(users__in=[profile]).count()

        new = events.exclude(users__in=[profile]).count()

        next_event = events.filter(users__in=[profile]).order_by('date_time').first()

        if next_event is not None:
            next_event = next_event.sample()

        unpaid = Money.moneys.exclude(users__in=[profile]).count()

        dashboard = Dashboard(new, going, next_event, unpaid)

        return Response(dashboard.__dict__)
