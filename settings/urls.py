from django.urls import path
from .views import *
from . import views


app_name = "settings"

urlpatterns = [
    path("", views.home, name="home"),
    path("services", views.services, name="services"),
    path("about_us", views.about_us, name="about_us"),
]
