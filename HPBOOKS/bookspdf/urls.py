from django.contrib import admin
from django.urls import path,include
from bookspdf import views
urlpatterns = [
    
    path("",views.join,name='join'),
    path("login",views.login,name='login'),
    path("hpb",views.hpb,name='hpb'),
]
