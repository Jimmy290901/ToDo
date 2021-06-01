
from django.contrib import admin
from django.urls import path, include
from tasks.views import home

urlpatterns = [
    path('',home),
]