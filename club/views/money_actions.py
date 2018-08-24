from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from club.models.action import MoneyRegisterForm
from club.models.money import Money
from club.models.user import Profile


class MoneyAction(APIView):
    permission_classes = (IsAuthenticated,)

    def handle(self, request, action):
        form = MoneyRegisterForm(request.data)

        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

        profile = get_object_or_404(Profile, pk=form.cleaned_data['user_id'])
        money = get_object_or_404(Money, pk=form.cleaned_data['money_id'])

        if not profile.user.id == request.user.id and not request.user.is_superuser:
            return Response('You can register for yourself only.', status=status.HTTP_403_FORBIDDEN)

        existing = money.users.filter(pk=profile.pk).exists()

        if action == 'POST':
            if not existing:
                money.users.add(profile)
                money.save()

        else:
            if existing:
                money.users.remove(profile)
                money.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        """
        Mark an user has already paid for a money
        """
        self.handle(request, 'POST')

    def delete(self, request):
        """
        Mark an user has not paid for a money
        """
        self.handle(request, 'DELETE')
