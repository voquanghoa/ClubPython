from django.contrib.auth.models import User
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from club.models.user import Profile, ProfileSerializer


class UserList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        profile = UserDetail.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

