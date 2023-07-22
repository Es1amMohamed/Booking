from django.urls import path
from .views import *

app_name = 'unit'

urlpatterns = [
    path('', unit_list, name = 'unit_list'),
    path('<slug:slug>',unit_detail, name = 'unit_detail')
]
