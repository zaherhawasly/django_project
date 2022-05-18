from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('room/',views.room,name="room"),
    path('room_details/<str:id>/',views.room_details,name="room_details")
]