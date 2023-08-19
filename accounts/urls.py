from django.urls import path , include
from . import views




app_name = 'accounts'

urlpatterns = [
    path('signup', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('reservation', views.my_reservation, name='my_reservation'),
    path('check/<int:id>', views.check_reservation, name='check_reservation'),
    path('cancel/<int:id>', views.cancel_reservation,name='cancel_reservation')
    
]