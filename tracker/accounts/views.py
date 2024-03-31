from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, UserLoginForm


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('')

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("accounts:login")
