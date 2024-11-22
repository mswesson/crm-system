from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
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


def get_ling_detail_or_statistics(user: User):
    groups_user = user.groups.values_list("name", flat=True)
    if groups_user in [settings.GROUPS[1], settings.GROUPS[1]]:
        link = reverse_lazy("advertising:advertising_detail")
    else:
        link = reverse_lazy("advertising:advertising_statistics")

    return link


class AdvertisingCompaniesList(LoginRequiredMixin, ListView):
    model = AdvertisingCompany
    template_name = "advertising/advertising_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs) -> dict:
        res = super().get_context_data(**kwargs)

        groups_user = self.request.user.groups.values_list("name", flat=True)
        if (
            settings.GROUPS[1] in groups_user
            or settings.GROUPS[3] in groups_user
        ):
            for adv in res["object_list"]:
                adv.link = reverse_lazy(
                    "advertising:advertising_detail", kwargs={"pk": adv.pk}
                )
        else:
            for adv in res["object_list"]:
                adv.link = reverse_lazy(
                    "advertising:advertising_statistics", kwargs={"pk": adv.pk}
                )

        return res

    def get_queryset(self):
        """
        Кастомная подгрузка объектов модели

        Реализовал поиск с помощью GET запроса с параметром 'search'
        """
        search = self.request.GET.get("search")
        queryset = super().get_queryset()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(service__title__icontains=search)
            )

        return queryset


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


class AdvertisingCompaniesStatisticsDetail(LoginRequiredMixin, DetailView):
    model = AdvertisingCompany
    template_name = "advertising/advertising_statistics.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        advertising: AdvertisingCompany = self.get_object()
        all_clients = advertising.clients
        active_clients = all_clients.filter(is_active=True)
        potential_clients = all_clients.filter(is_active=False)
        company_profit = sum(
            [client.contract.budget for client in active_clients]
        )
        advertising_roi = f"{company_profit / advertising.budget:.2%}"

        context = {
            "object": advertising,
            "all_clients": all_clients,
            "potential_clients": potential_clients,
            "active_clients": active_clients,
            "company_profit": company_profit,
            "advertising_roi": advertising_roi,
        }

        return render(request, self.template_name, context)


class AdvertisingCompaniesDetail(
    UserPassesTestMixin, AdvertisingCompaniesStatisticsDetail
):
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
