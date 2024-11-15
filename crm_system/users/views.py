from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def users_homepage(request: HttpRequest):
    return HttpResponse("<h1>Users homepage</h1>")


class UserDetailView(DetailView):
    """Личный кабинет пользователя"""

    model = User
    template_name = "users/user_profile.html"

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        user = get_object_or_404(User, pk=kwargs.get("pk"))
        context = {"object": user}
        return render(request, self.template_name, context)
