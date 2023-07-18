from django.urls import path
from .views import Registration, Login


app_name = 'accounts'

urlpatterns = [
    path('join/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]
