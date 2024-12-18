from django.urls import path, include
from . import views
from .api_views import api_profile


app_name = "accounts"

urlpatterns = [ 
    path("signup", views.sign_up, name="signup"),
    path('logout/', views.log_out, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("reservation", views.my_reservation, name="my_reservation"),
    path("check/<int:id>", views.check_reservation, name="check_reservation"),
    path("cancel/<int:id>", views.cancel_reservation, name="cancel_reservation"),
    path("password/change", views.change_password, name="change_password"),
    # api
    # path("api/profile", api_profile, name="api_profile"),
    path("api/profile", api_profile, name="api_profile"),
]
