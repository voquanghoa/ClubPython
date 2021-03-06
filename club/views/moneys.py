from django.http import Http404, JsonResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from club.models.money import MoneySerializer, Money


class MoneyList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Get all moneys
        """
        return Response(MoneySerializer(Money.moneys.all(), many=True).data)

    def post(self, request):
        """
        Create a new money
        """
        serializer = MoneySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return HttpResponseBadRequest()


class MoneyView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Money.objects.get(pk=pk)
        except Money.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Get a money by id
        """
        money = self.get_object(pk)
        return Response(MoneySerializer(money).data)

    def put(self, request, pk):
        """
        Update an money by id
        """
        event = self.get_object(pk)
        serializer = MoneySerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a money
        """
        money = self.get_object(pk)
        money.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)