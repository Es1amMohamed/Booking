from django.urls import path
from . import views
app_name = "amadeus"

urlpatterns = [
    path("", views.all_hotels_view, name="all_hotels"),
    path("hotel_detail/<str:hotelId>/", views.hotel_detail_view, name="hotel_detail"),
]