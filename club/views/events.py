import datetime

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from club.decorators.require_super_user import superuser_only, has_profile
from club.models.event import Event, EventSerializer


class EventList(APIView):
    permission_classes = (IsAuthenticated,)

    @has_profile
    def get(self, request, event_type):
        profile = request.profile
        events = Event.events

        if not event_type == 'all':
            if event_type == 'past':
                events = events.filter(date_time__lte=datetime.date.today())
            else:
                events = events.filter(date_time__gte=datetime.date.today())

            if event_type == 'going':
                events = events.filter(users__in=[profile])

            if event_type == 'new':
                events = events.exclude(users__in=[profile])

        return Response(EventSerializer(events, many=True).data)


class EventPost(APIView):
    permission_classes = (IsAuthenticated,)

    @superuser_only
    def post(self, request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return HttpResponseBadRequest()

    def get(self, request):
        events = Event.events
        return Response(EventSerializer(events, many=True).data)


class EventView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Event.events.filter(pk=pk))

    def get(self, request, pk):
        event = self.get_object(pk)
        return Response(EventSerializer(event).data)

    @superuser_only
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @superuser_only
    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)