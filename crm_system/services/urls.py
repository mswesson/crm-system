from django.urls import path
from .views import (
    ServicesListView,
    ServicesCreateView,
    ServicesUpdateView,
    ServicesDeleteConfirmView,
    ServicesDeleteView,
    ServicesDetailView,
)

app_name = "services"

urlpatterns = [
    path("", ServicesListView.as_view(), name="services_list"),
    path("create/", ServicesCreateView.as_view(), name="services_create"),
    path(
        "update/<int:pk>", ServicesUpdateView.as_view(), name="services_update"
    ),
    path(
        "delete/<int:pk>", ServicesDeleteView.as_view(), name="services_delete"
    ),
    path(
        "delete/<int:pk>/confirm",
        ServicesDeleteConfirmView.as_view(),
        name="services_confirm_delete",
    ),
    path("<int:pk>/", ServicesDetailView.as_view(), name="services_detail"),
]
