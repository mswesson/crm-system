from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)

from .models import AdvertisingCompany
from .forms import AdvertisingCompanyForm


class AdvertisingCompaniesList(
    LoginRequiredMixin, UserPassesTestMixin, ListView
):
    model = AdvertisingCompany
    template_name = "advertising/advertising_list.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes


class AdvertisingCompaniesCreate(
    LoginRequiredMixin, UserPassesTestMixin, CreateView
):
    model = AdvertisingCompany
    form_class = AdvertisingCompanyForm
    template_name = "advertising/advertising_create.html"
    success_url = reverse_lazy("advertising:advertising_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes


class AdvertisingCompaniesUpdate(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = AdvertisingCompany
    form_class = AdvertisingCompanyForm
    template_name = "advertising/advertising_update.html"
    success_url = reverse_lazy("advertising:advertising_update")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes


class AdvertisingCompaniesDetail(
    LoginRequiredMixin, UserPassesTestMixin, DetailView
):
    model = AdvertisingCompany
    template_name = "advertising/advertising_detail.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes


class AdvertisingCompaniesDeleteConfirmView(
    LoginRequiredMixin, UserPassesTestMixin, View
):
    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        service = AdvertisingCompany.objects.get(pk=pk)
        context = {"object": service}
        return render(
            request, "advertising/advertising_confirm_delete.html", context
        )

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes


class AdvertisingCompaniesDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = AdvertisingCompany
    success_url = reverse_lazy("advertising:advertising_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[3]]
        ).exists()
        return passes
