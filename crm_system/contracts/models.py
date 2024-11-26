from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.files import File
import random

from .pdf_creator import create_pdf_doc


def upload_documentation_title(instance: "Contract", filename: str) -> str:
    service_pk = instance.service
    full_name = (
        f"contracts/documentations/service_id{service_pk}/doc_{filename}"
    )
    return full_name


class Contract(models.Model):
    """
    Контракт

    Хранит информацию:
        название
        предоставляемую услугу (связь с Услугой)
        клиент (связь с клиентом)
        файл с документом
        дату заключения (автоматически создается при создании)
        период действия (до какого числа и года)
        сумму
    """

    title = models.CharField(
        max_length=100, unique=True, null=False, blank=False, db_index=True
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="contracts",
    )
    client = models.OneToOneField(
        "clients.Client",
        on_delete=models.CASCADE,
        null=False,
        related_name="contract",
    )
    documentation = models.FileField(
        null=True, upload_to="contracts/documentations/", blank=True
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=False, blank=False)
    budget = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0, "The contract amount cannot be below zero")
        ],
    )

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        #  Создаю файл договора, если его нет
        if not self.documentation:
            full_name_clients = (
                f"{self.client.first_name} {self.client.last_name}"
            )
            file_name = (
                f"{random.randint(100, 10000)}_"
                f"{self.client.first_name}_"
                f"{self.client.last_name}_"
                f"{self.service.title}.pdf"
            )
            file_path = create_pdf_doc(
                company_name=settings.COMPANY_NAME,
                full_name_client=full_name_clients,
                start_date=self.start_date.date(),
                end_date=self.end_date.date(),
                budget=self.budget,
                save_path=(
                    settings.MEDIA_ROOT
                    / f"contracts/documentations/{file_name}"
                ),
            )

            with open(file_path, "rb") as file_doc:
                self.documentation.save(file_name, file_doc, save=False)

        return super().save()

    class Meta:
        ordering = ["start_date", "pk"]

    def __str__(self) -> str:
        full_title = f"{self.title} ({self.pk})"
        return full_title
