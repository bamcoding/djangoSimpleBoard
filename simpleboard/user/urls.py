from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('login/', v.login),
    path('dologin/', v.dologin),
    path('signup/', v.signup),
    path('dosignup/', v.dosignup),
]