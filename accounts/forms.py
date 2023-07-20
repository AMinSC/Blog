from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="아이디")
    
    class Meta:
        model = User
        fields = ['username']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="아이디")
    
    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'email']
