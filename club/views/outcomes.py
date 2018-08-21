from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from club.decorators.require_super_user import superuser_only
from club.models.outcome import Outcome, OutcomeSerializer


class OutcomeList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(OutcomeSerializer(Outcome.outcomes.all(), many=True).data)

    @superuser_only
    def post(self, request):
        serializer = OutcomeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return HttpResponseBadRequest()


class OutcomeView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Outcome, pk=pk)

    def get(self, request, pk):
        return Response(OutcomeSerializer(self.get_object(pk)).data)

    @superuser_only
    def put(self, request, pk):
        serializer = OutcomeSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @superuser_only
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)