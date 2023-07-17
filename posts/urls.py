from django.contrib import admin
from django.urls import path, include
from .views import PostView


app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='list'),
]
