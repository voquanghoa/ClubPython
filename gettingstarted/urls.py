from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

admin.autodiscover()

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),

    path('admin', admin.site.urls),

    url(r'^api', include('club.urls')),
    url(r'', include_docs_urls(title='Club API'))
]
