from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='Project-Home'),
    path('about/',views.about, name ='Project-About'),
    path('reservation/',views.reservation, name ='Project-Reservation'),
    path('schedule/',views.schedule, name ='Project-Schedule'),
]