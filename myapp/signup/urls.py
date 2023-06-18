from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',login),
    path('signup/',signup),
    path('signup/user/',signup_user),
    path('signin_user/',signin_user) 
]