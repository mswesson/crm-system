from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
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


class AdvertisingCompaniesList(ListView):
    model = AdvertisingCompany
    template_name = "advertising/advertising_list.html"


class AdvertisingCompaniesCreate(CreateView):
    model = AdvertisingCompany
    form_class = AdvertisingCompanyForm
    template_name = "advertising/advertising_create.html"
    success_url = reverse_lazy("advertising:advertising_list")


class AdvertisingCompaniesUpdate(UpdateView):
    model = AdvertisingCompany
    form_class = AdvertisingCompanyForm
    template_name = "advertising/advertising_update.html"
    success_url = reverse_lazy("advertising:advertising_update")


class AdvertisingCompaniesDetail(DetailView):
    model = AdvertisingCompany
    template_name = "advertising/advertising_detail.html"


class AdvertisingCompaniesDeleteConfirmView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        service = AdvertisingCompany.objects.get(pk=pk)
        context = {"object": service}
        return render(
            request, "advertising/advertising_confirm_delete.html", context
        )


class AdvertisingCompaniesDeleteView(DeleteView):
    model = AdvertisingCompany
    success_url = reverse_lazy("advertising:advertising_list")
