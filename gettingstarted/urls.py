from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import club.views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^$', club.views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
