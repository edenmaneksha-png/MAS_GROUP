from django.urls import path
from .views import *

app_name = "masgroupapp"

urlpatterns = [
    path("", v1, name="v1"),
    path("v1about/", v1about, name="v1about"),
    path("v1form/", v1form, name="v1form"),
    path("v1aca/", v1aca, name="v1aca"),
    path("v1fees/", v1fees, name="v1fees"),
]