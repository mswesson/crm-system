from django.urls import path

from .views import (
    PotentialClientListView,
    PotentialClientDetailView,
    PotentialClientUpdateView,
    PotentialClientDeleteView,
    PotentialClientDeleteConfirmView,
    PotentialClientCreateApiView,
    ActiveClientListView,
    ActiveClientDetailView,
    ActiveClientUpdateView,
)

app_name = "clients"

urlpatterns = [
    path(
        "potential/", PotentialClientListView.as_view(), name="potential_list"
    ),
    path(
        "potential/<int:pk>/",
        PotentialClientDetailView.as_view(),
        name="potential_detail",
    ),
    path(
        "potential/<int:pk>/update/",
        PotentialClientUpdateView.as_view(),
        name="potential_update",
    ),
    path(
        "potential/<int:pk>/delete/",
        PotentialClientDeleteView.as_view(),
        name="potential_delete",
    ),
    path(
        "potential/<int:pk>/delete/confirm/",
        PotentialClientDeleteConfirmView.as_view(),
        name="potential_delete_confirm",
    ),
    path(
        "potential/api/",
        PotentialClientCreateApiView.as_view(),
        name="potential_api",
    ),
    path("active/", ActiveClientListView.as_view(), name="active_list"),
    path(
        "active/<int:pk>/",
        ActiveClientDetailView.as_view(),
        name="active_detail",
    ),
    path(
        "active/<int:pk>/update/",
        ActiveClientUpdateView.as_view(),
        name="active_update",
    ),
]
