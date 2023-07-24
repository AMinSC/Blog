from django.urls import path
from .views import PostView, PostDetail, PostWrite, PostEdit, PostDelete, PostSerach, CommentWrite


app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='list'),
    path('<int:post_id>/', PostDetail.as_view(), name='detail'),
    path('write/', PostWrite.as_view(), name='write'),
    path('<int:post_id>/edit/', PostEdit.as_view(), name='edit'),
    path('<int:post_id>/delete/', PostDelete.as_view(), name='delete'),
    path('search/', PostSerach.as_view(), name='search'),
    path('<int:post_id>/comment/write/', CommentWrite.as_view(), name='cm-write'),
]
