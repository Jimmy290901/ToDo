from user.views import login, signup
from django.urls import path, include

urlpatterns = [
    path('',login),
    path('signup',signup),
]