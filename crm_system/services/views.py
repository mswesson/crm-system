from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    DetailView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Service
from .forms import ServiceForm


class ServicesListView(ListView):
    """
    Список услуг

    Имеет ограничение доступа, могут видеть только маркетологи
    """

    model = Service
    template_name = "services/services_list.html"
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
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        return queryset


class ServicesCreateView(CreateView):
    """
    Создание новой услуги

    Имеет ограничение доступа, могут создавать только маркетологи
    """

    model = Service
    template_name = "services/services_create.html"
    form_class = ServiceForm
    success_url = reverse_lazy("services:services_list")


class ServicesUpdateView(UpdateView):
    """
    Изменение существующей услуги

    Имеет ограничение доступа, могут изменять только маркетологи
    """

    model = Service
    template_name = "services/services_update.html"
    form_class = ServiceForm
    success_url = reverse_lazy("services:services_list")


class ServicesDeleteConfirmView(View):
    """
    Подтверждение удаления

    Имеет ограничение доступа, могут удалять только маркетологи
    """

    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        service = Service.objects.get(pk=pk)
        context = {"object": service}
        return render(
            request, "services/services_confirm_delete.html", context
        )


class ServicesDeleteView(DeleteView):
    """
    Удаление существующей услуги

    Имеет ограничение доступа, могут удалять только маркетологи
    """

    model = Service
    success_url = reverse_lazy("services:services_list")


class ServicesDetailView(DetailView):
    """Личный кабинет пользователя"""

    model = Service
    template_name = "services/service_detail.html"
