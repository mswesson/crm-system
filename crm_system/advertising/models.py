from django.db import models
from django.core.validators import MinValueValidator


class AdvertisingCompany(models.Model):
    """
    Рекламная компания

    Хранит в себе информацию:
        название рекламной кампании
        рекламируемую услугу (связь один ко многим с Услугой)
        канал продвижения
        бюджет на рекламу
    """

    title = models.CharField(
        max_length=100, unique=True, null=False, blank=False, db_index=True
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="advertising_companies",
    )
    promotion_channel = models.CharField(
        max_length=100, null=False, blank=False, db_index=True
    )
    budget = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0, "The price cannot be below zero")],
    )
