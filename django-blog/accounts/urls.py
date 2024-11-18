from django.urls import path
from .views import Registration, Login, Logout, Update, PasswordChange


app_name = 'accounts'

urlpatterns = [
    path('join/', Registration, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('update/', Update, name='update'),
    path('update/pw-change', PasswordChange, name='pw-change'),
]
