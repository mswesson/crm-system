from django.urls import path

from .views import (
    AdvertisingCompaniesList,
    AdvertisingCompaniesCreate,
    AdvertisingCompaniesUpdate,
    AdvertisingCompaniesDetail,
    AdvertisingCompaniesDeleteConfirmView,
    AdvertisingCompaniesDeleteView,
    AdvertisingCompaniesStatisticsDetail,
)

app_name = "advertising"

urlpatterns = [
    path("", AdvertisingCompaniesList.as_view(), name="advertising_list"),
    path(
        "create/",
        AdvertisingCompaniesCreate.as_view(),
        name="advertising_create",
    ),
    path(
        "<int:pk>/",
        AdvertisingCompaniesDetail.as_view(),
        name="advertising_detail",
    ),
    path(
        "<int:pk>/statistics/",
        AdvertisingCompaniesStatisticsDetail.as_view(),
        name="advertising_statistics",
    ),
    path(
        "<int:pk>/update/",
        AdvertisingCompaniesUpdate.as_view(),
        name="advertising_update",
    ),
    path(
        "<int:pk>/delete/",
        AdvertisingCompaniesDeleteView.as_view(),
        name="advertising_delete",
    ),
    path(
        "<int:pk>/delete/confirm/",
        AdvertisingCompaniesDeleteConfirmView.as_view(),
        name="advertising_delete_confirm",
    ),
]
