from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm


class Registration(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:list')
        return super().get(request, *args, **kwargs)

### Login
class Login(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        print(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:list')
        return super().get(request, *args, **kwargs)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')
