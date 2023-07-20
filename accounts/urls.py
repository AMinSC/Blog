from django.urls import path
from .views import Registration, Login, Logout, Update


app_name = 'accounts'

urlpatterns = [
    path('join/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('update/', Update.as_view(), name='update'),
]
