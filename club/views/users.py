from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from club.decorators.require_super_user import has_profile
from club.models.user import Profile, ProfileSerializer
from club.utils.responses import object_response


class UserList(APIView):

    def get(self, request):
        """
        Get all users
        """
        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)

    def post(self, request):
        """
        Create a new user
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @has_profile
    def put(self, request):
        """
        Update an user (change avatar)
        """
        serializer = ProfileSerializer(request.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeDetail(APIView):

    @has_profile
    def get(self, request):
        """
        Get information of the current logged in user
        """
        return object_response(ProfileSerializer(request.profile).data)
