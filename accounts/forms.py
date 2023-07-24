from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100, disabled=True, label="아이디")
    nickname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.nickname = self.cleaned_data.get('nickname')
        user.email = self.cleaned_data.get('email')
        
        if commit:
            user.save()
        
        return user


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
