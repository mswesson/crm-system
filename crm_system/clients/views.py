from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.db.models import Value
from django.db.models.functions import Concat
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)

from .models import Client
from .forms import ClientForm
from .serializers import ClientSerializer


# Potential clients


class PotentialClientListView(
    LoginRequiredMixin, UserPassesTestMixin, ListView
):
    model = Client
    template_name = "clients/clients_potential_list.html"
    paginate_by = 5

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[
                settings.GROUPS[1],
                settings.GROUPS[2],
                settings.GROUPS[4],
            ]
        ).exists()
        return passes

    def get_queryset(self):
        """
        Кастомная подгрузка объектов модели

        Реализовал поиск с помощью GET запроса с параметром 'search'
        """
        search = self.request.GET.get("search")
        today_interaction_clients = (
            self.request.GET.get("today_interaction", "false") == "true"
        )

        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=False)

        if search:
            queryset = queryset.annotate(
                full_name=Concat("first_name", Value(" "), "last_name")
            ).filter(
                Q(full_name__icontains=search)
                | Q(phone_number__icontains=search)
                | Q(email__icontains=search)
            )

        if today_interaction_clients:
            start_day = timezone.now().date()
            end_of_day = start_day + timedelta(days=1)
            queryset = queryset.filter(
                next_interaction_date__gte=start_day,
                next_interaction_date__lt=end_of_day,
            )

        return queryset


class PotentialClientDetailView(
    LoginRequiredMixin, UserPassesTestMixin, DetailView
):
    model = Client
    template_name = "clients/clients_potential_detail.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[
                settings.GROUPS[1],
                settings.GROUPS[2],
                settings.GROUPS[4],
            ]
        ).exists()
        return passes

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=False)
        return queryset


class PotentialClientUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Client
    form_class = ClientForm
    template_name = "clients/clients_potential_update.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[
                settings.GROUPS[1],
                settings.GROUPS[2],
                settings.GROUPS[4],
            ]
        ).exists()
        return passes

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=False)
        return queryset

    def get_success_url(self):
        return reverse_lazy(
            "clients:potential_detail", kwargs={"pk": self.object.pk}
        )


class PotentialClientDeleteConfirmView(
    LoginRequiredMixin, UserPassesTestMixin, View
):
    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[2]]
        ).exists()
        return passes

    def get(self, request: HttpRequest, *args, **kwargs):
        pk = self.kwargs.get("pk")
        service = Client.objects.get(pk=pk, is_active=False)
        context = {"object": service}
        return render(
            request, "clients/clients_potential_delete_confirm.html", context
        )


class PotentialClientDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = Client
    success_url = reverse_lazy("clients:potential_list")

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[2]]
        ).exists()
        return passes

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=False)
        return queryset


class PotentialClientCreateApiView(APIView):
    def get(self, request: Request) -> Response:
        clients = Client.objects.filter(is_active=False)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ClientSerializer(data=request.data)
        request_token = request.headers.get("Token")

        if request_token not in settings.TOKENS_API:
            return Response(
                {"token_errors": "Token is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Active clients


class ActiveClientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Client
    template_name = "clients/clients_active_list.html"
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
        queryset = queryset.filter(is_active=True)

        if search:
            queryset = queryset.annotate(
                full_name=Concat("first_name", Value(" "), "last_name")
            ).filter(
                Q(full_name__icontains=search)
                | Q(phone_number__icontains=search)
                | Q(email__icontains=search)
            )

        return queryset


class ActiveClientDetailView(DetailView):
    model = Client
    template_name = "clients/clients_active_detail.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class ActiveClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "clients/clients_active_update.html"

    def test_func(self) -> bool | None:
        passes = self.request.user.groups.filter(
            name__in=[settings.GROUPS[1], settings.GROUPS[4]]
        ).exists()
        return passes

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

    def get_success_url(self):
        return reverse_lazy(
            "clients:active_detail", kwargs={"pk": self.object.pk}
        )
