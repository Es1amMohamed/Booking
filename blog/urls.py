from . import views
from django.urls import path
from .views import *
from .api_view import *

app_name = "blog"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<slug:slug>", views.post_detail, name="post_detail"),
    # api
    path("api/list", post_list_api, name="post_list_api"),
    path("api/<int:id>", post_detail_api, name="post_detail_api"),
    path("api/filter/<str:query>", post_search_api, name="post_search_api"),
]
