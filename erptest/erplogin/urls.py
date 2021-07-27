from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.connsql, name='connsql'),
    path('loginuser',views.loginuser, name='loginuser'),
]
