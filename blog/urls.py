from django.contrib import admin
from django.urls import path, include
from .views import IndexView


app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('blog/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
]
