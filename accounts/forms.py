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


class ProfileForm(PasswordChangeForm):
    nickname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2', 'nickname', 'email']

    def save(self, commit=True):
        # password is updated by the original save method
        user = super().save(commit=False)
        
        # here we update the additional fields
        user.nickname = self.cleaned_data.get('nickname')
        user.email = self.cleaned_data.get('email')
        
        if commit:
            user.save()
        
        return user
