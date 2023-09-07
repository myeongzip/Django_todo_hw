from django.contrib import admin
from django.urls import include, path

from todo import views


urlpatterns = [
    path('create/', views.create),
    path('read/', views.read),
    path('update/', views.update),
    path('delete/', views.delete),
]