from django.urls import path
from .views import PostView, PostDetail, PostWrite, PostEdit, PostDelete, PostSerach, CommentWrite, CommentDelete, ReCommentWrite, ReCommentDelete


app_name = 'blog'

urlpatterns = [
    path('', PostView, name='list'),
    path('<int:post_id>/', PostDetail, name='detail'),
    path('write/', PostWrite, name='write'),
    path('<int:post_id>/edit/', PostEdit, name='edit'),
    path('<int:post_id>/delete/', PostDelete, name='delete'),
    path('search/', PostSerach, name='search'),
    path('<int:post_id>/comment/write/', CommentWrite, name='cm-write'),
    path('<int:post_id>/comment/<int:pk>/delete/', CommentDelete, name='cm-delete'),
    path('<int:post_id>/comment/<int:comment_id>/recomment/write/', ReCommentWrite, name='recomment-write'),
    path('<int:post_id>/ReComment/<int:pk>/delete', ReCommentDelete, name='recomment-delete'),
]
