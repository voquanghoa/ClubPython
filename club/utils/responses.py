from rest_framework import status
from rest_framework.response import Response


def object_response(obj):
    return Response(obj, status=status.HTTP_200_OK)


def model_response(obj):
    return object_response(obj.__dict__)