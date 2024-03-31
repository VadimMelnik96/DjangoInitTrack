from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserLoginView, UserRegistrationView

app_name = "accounts"

urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]