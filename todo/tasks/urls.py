
from django.contrib import admin
from django.urls import path, include
from tasks.views import home, updateTask

urlpatterns = [
    path('',home),
    path('update/<int:task_id>', updateTask, name='updateTask'),
]