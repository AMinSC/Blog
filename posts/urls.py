from django.contrib import admin
from django.urls import path, include
from .views import PostView, PostDetail, PostWrite


app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='list'),
    path('<int:post_id>/', PostDetail.as_view(), name='detail'),
    path('write/', PostWrite.as_view(), name='write'),
]
