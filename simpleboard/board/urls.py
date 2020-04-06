from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('main/', v.main),
    path('edit/', v.edit),
    path('add/', v.add),
    path('remove/', v.remove),
]
