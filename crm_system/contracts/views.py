from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import make_aware
from django.db.models import Q
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)

from .models import Contract
from .forms import ContractForm


class ContractsListView(ListView):
    model = Contract
    template_name = "contracts/contracts_list.html"
    paginate_by = 3

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


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts_create.html"
    success_url = reverse_lazy("contracts:contracts_list")


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts_update.html"
    success_url = reverse_lazy("contracts:contracts_list")


class ContractDetailView(DetailView):
    model = Contract
    template_name = "contracts/contracts_detail.html"


class ContractDeleteConfirmView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        contract = Contract.objects.get(pk=pk)
        context = {"object": contract}
        return render(
            request, "contracts/contracts_confirm_delete.html", context
        )


class ContractDeleteView(DeleteView):
    model = Contract
    success_url = reverse_lazy("contracts:contracts_list")
