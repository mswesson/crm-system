from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from clients.models import Client
from django.core.exceptions import ValidationError
from django.utils import timezone
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

from clients.models import Client
from services.models import Service
from .models import Contract
from .forms import ContractForm


class ContractsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Contract
    template_name = "contracts/contracts_list.html"
    paginate_by = 3

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes

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


class ContractCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts_create.html"
    success_url = reverse_lazy("contracts:contracts_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes

    def get_initial(self):
        client_pk = self.request.GET.get("client_pk")
        service_pk = self.request.GET.get("service_pk")
        service = Service.objects.get(pk=service_pk)
        client = Client.objects.get(pk=client_pk)

        initial = super().get_initial()

        initial["title"] = (
            f"{client.last_name[:1]}. {client.first_name} "
            f"({timezone.now().date()}) - {service.title}"
        )
        initial["client"] = client_pk
        initial["service"] = service_pk
        initial["budget"] = service.price
        return initial

    def form_valid(self, form):
        client_pk = form.data.get("client")
        client = Client.objects.get(pk=client_pk)

        if not client:
            raise ValidationError("Client not found")
        if client.is_active:
            raise ValidationError("The client must be inactive")

        end_date = form.data.get("end_date")

        client.next_interaction_date = end_date
        client.is_active = True
        client.notes += f"\n- The contract has been signed ({timezone.now()})"
        client.save()
        return super().form_valid(form)


class ContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts_update.html"
    success_url = reverse_lazy("contracts:contracts_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes


class ContractDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Contract
    template_name = "contracts/contracts_detail.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes


class ContractDeleteConfirmView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        contract = Contract.objects.get(pk=pk)
        context = {"object": contract}
        return render(
            request, "contracts/contracts_confirm_delete.html", context
        )

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes


class ContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contract
    success_url = reverse_lazy("contracts:contracts_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes

    def form_valid(self, form):
        object: Contract = self.object
        object.client.is_active = False
        object.client.next_interaction_date = timezone.now()
        object.client.notes += (
            f"\n- The contract has been terminated ({timezone.now()})"
        )
        object.client.save()
        return super().form_valid(form)
