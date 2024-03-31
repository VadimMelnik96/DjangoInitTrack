from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="main"),
    path("accounts/", include("accounts.urls", "accounts")),
]
