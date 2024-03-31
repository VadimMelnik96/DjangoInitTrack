from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "email"]



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]





