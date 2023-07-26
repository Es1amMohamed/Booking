from . import views
from django.urls import path
from .views import *

app_name = 'blog'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail' ),
]