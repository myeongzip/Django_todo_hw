from django.contrib import admin
from django.urls import include, path

from todo import views


urlpatterns = [
    path('index/', views.todo_index),
    path('create/', views.todo_create),
    path('read/', views.todo_read),
    path('update/', views.todo_update),
    path('delete/', views.todo_delete),
]