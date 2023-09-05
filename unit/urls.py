from . import views
from django.urls import path
from .views import *
from .api_view import *

app_name = "unit"

urlpatterns = [
    path("", views.unit_list, name="unit_list"),
    path("<slug:slug>", views.unit_detail, name="unit_detail"),
    # api
    path("api/", UnitAPIList.as_view(), name="unit_api_list"),
    path("api/<int:pk>", UnitAPIdetail.as_view(), name="unit_api_detail"),
    path(
        "api/create_reservation/",
        CreateReservationAPI.as_view(),
        name="create_reservation_api",
    ),
    path(
        "api/reservation/<int:id>", reservation_detail_api, name="unit_api_reservation"
    ),
]
