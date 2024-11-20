from django.urls import path

from .views import (
    ContractsListView,
    ContractCreateView,
    ContractUpdateView,
    ContractDetailView,
    ContractDeleteConfirmView,
    ContractDeleteView,
)

app_name = "contracts"

urlpatterns = [
    path("", ContractsListView.as_view(), name="contracts_list"),
    path("create/", ContractCreateView.as_view(), name="contracts_create"),
    path("<int:pk>/", ContractDetailView.as_view(), name="contracts_detail"),
    path(
        "<int:pk>/update/",
        ContractUpdateView.as_view(),
        name="contracts_update",
    ),
    path(
        "<int:pk>/delete/",
        ContractDeleteView.as_view(),
        name="contracts_delete",
    ),
    path(
        "<int:pk>/delete/confirm/",
        ContractDeleteConfirmView.as_view(),
        name="contracts_delete_confirm",
    ),
]
