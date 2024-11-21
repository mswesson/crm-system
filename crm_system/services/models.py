from django.db import models
from django.core.validators import MinValueValidator


class Service(models.Model):
    """
    Услуга

    Хранит в себе информацию об услуге:
        название
        описание
        стоимость
    """

    title = models.CharField(
        max_length=100, unique=True, null=False, blank=False, db_index=True
    )
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0, "The price cannot be below zero")],
    )

    def short_description(self):
        return self.description[:140] + "..."

    def __str__(self):
        full_title = f"{self.pk} - {self.title}"
        return full_title
