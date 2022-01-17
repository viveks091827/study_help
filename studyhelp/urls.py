
from django.contrib import admin
from django.http.response import HttpResponsePermanentRedirect
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]
