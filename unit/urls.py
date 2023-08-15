from . import views
from django.urls import path
from .views import *

app_name = 'unit'

urlpatterns = [
    path('', views.unit_list, name = 'unit_list'),
    path('<slug:slug>',views.unit_detail, name = 'unit_detail'),
]
