from django.urls import path
from .views import users_homepage, UserDetailView

app_name = "users"

urlpatterns = [
    path("", users_homepage, name="homepage"),
    path("profile/<int:pk>", UserDetailView.as_view(), name="profile"),
]
