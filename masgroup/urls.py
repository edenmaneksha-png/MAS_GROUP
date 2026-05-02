from django.contrib import admin
from django.urls import path, include
from masgroupapp.views import v1form

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("masgroupapp.urls")),
     path('submit-admission/', v1form, name='admission'),
]
