from django.http import JsonResponse, HttpResponse

from club.models import Event


def events(request):

    if request.method == 'GET':
        events = Event.objects.all()
        return HttpResponse(events)
