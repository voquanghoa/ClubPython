from rest_framework.views import APIView
from rest_framework.response import Response

from club.models.event import Event, EventSerializer


class EventView(APIView):
    def get(self, request):
        return Response(EventSerializer(Event.objects.all(), many=True).data)
