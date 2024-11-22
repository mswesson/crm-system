from django.db import models
from django.forms import ValidationError
from django.utils import timezone
import re


def validate_phone_number(value):
    if not re.match(r"^\+\d{9,15}$", value):
        raise ValidationError(
            'Please enter a valid phone number that starts with "+"'
        )


class Client(models.Model):
    """
    Модель потенциального клиента

    Хранит в себе:
        Имя
        Фамилия
        Отчество (может отсутствовать)
        телефон
        email
        рекламную кампанию, из которой он узнал об услуге
    """

    first_name = models.CharField(
        max_length=50, null=False, blank=False, db_index=True
    )
    last_name = models.CharField(
        max_length=50, null=False, blank=False, db_index=True
    )
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[validate_phone_number],
    )
    email = models.EmailField(null=False, blank=False, db_index=True)
    advertising_company = models.ForeignKey(
        "advertising.AdvertisingCompany",
        on_delete=models.CASCADE,
        related_name="clients",
    )
    notes = models.TextField(
        max_length=4000, default="", null=False, blank=True
    )
    next_interaction_date = models.DateTimeField(
        default=timezone.now, null=False, blank=True
    )
    is_active = models.BooleanField(null=False, blank=True, default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "first_name",
                    "last_name",
                    "middle_name",
                    "phone_number",
                    "email",
                    "advertising_company",
                ],
                name="unique_field_combination",
            )
        ]
        ordering = ["next_interaction_date"]

    def __str__(self) -> str:
        full_name = (
            f"{self.pk} - "
            f"{self.first_name} "
            f"{self.middle_name if self.middle_name else ''} "
            f"{self.last_name}"
            )
        return full_name
