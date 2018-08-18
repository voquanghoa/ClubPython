from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
import club.views
from rest_framework_jwt.views import obtain_jwt_token

admin.autodiscover()

urlpatterns = [
    url(r'^$', club.views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),

    url(r'^events', include('club.urls'))
]
