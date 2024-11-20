from django.core.validators import MinValueValidator

from django.db import models


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
    documentation = models.FileField(
        null=True, upload_to="contracts/documentations/"
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
