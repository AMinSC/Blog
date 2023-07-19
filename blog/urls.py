from django.contrib import admin
from django.urls import path, include
from .views import IndexView

from django.conf.urls.static import static
from django.conf import settings


app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('blog/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
]
# img
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
