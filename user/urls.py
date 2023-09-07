from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('signup/', views.user_signup),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
]