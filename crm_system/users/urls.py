from django.urls import path
from .views import (
    UserDetailView,
    UserLoginView,
    UserLogoutView,
)

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", UserDetailView.as_view(), name="profile"),
]
