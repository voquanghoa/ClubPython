from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from club.models.action import RegisterForm
from club.models.event import Event
from club.models.user import Profile


class EventAction(APIView):
    permission_classes = (IsAuthenticated,)

    @classmethod
    def handle(cls, request, action):
        form = RegisterForm(request.data)

        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

        profile = get_object_or_404(Profile, pk=form.cleaned_data['user_id'])
        event = get_object_or_404(Event, pk=form.cleaned_data['event_id'])

        if not profile.user.id == request.user.id and not request.user.is_superuser:
            return Response('You can register for yourself only.', status=status.HTTP_403_FORBIDDEN)

        existing = event.users.filter(pk=profile.pk).exists()

        if action == 'POST':
            if not existing:
                event.users.add(profile)
                event.save()

        else:
            if existing:
                event.users.remove(profile)
                event.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        return EventAction.handle(request, 'DELETE')

    def post(self, request):
        return EventAction.handle(request, 'POST')

