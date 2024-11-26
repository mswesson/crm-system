from django.core.management import BaseCommand
import random
from django.utils import timezone
from datetime import datetime, timedelta

from clients.models import Client
from advertising.models import AdvertisingCompany


class Command(BaseCommand):
    """Создает клиентов"""

    def random_date(self) -> datetime:
        """Рандомная дата в пределах двух дней только в прошлое"""
        now = timezone.now()
        delta = timedelta(days=2)
        random_offset = random.uniform(0, delta.total_seconds())
        result_data = now - timedelta(seconds=random_offset)
        return result_data

    def handle(self, *args, **options):
        self.stdout.write("Start of advertising creation")

        first_names = [
            "John",
            "Emily",
            "Michael",
            "Sophia",
            "Daniel",
            "Olivia",
            "James",
            "Emma",
            "Benjamin",
            "Ava",
            "William",
            "Mia",
        ]

        last_names = [
            "Smith",
            "Johnson",
            "Brown",
            "Williams",
            "Jones",
            "Garcia",
            "Miller",
            "Davis",
            "Martinez",
            "Hernandez",
            "Lopez",
            "Clark",
        ]

        middle_names = [
            "James",
            "Marie",
            "Lee",
            "Grace",
            "Alexander",
            "Rose",
            "David",
            "Elizabeth",
            "Joseph",
            "Anne",
            None,
        ]

        domains = ["example.com", "mail.com", "outlook.com", "gmail.com"]

        try:
            advertising_companies = list(AdvertisingCompany.objects.all())
        except AdvertisingCompany.DoesNotExist:
            self.stdout.write("The advertising were not created in advance")
            return

        for _ in range(50):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            middle_name = random.choice(middle_names)
            phone_number = (
                f"+7-9{random.randint(10, 99)}-"
                f"{random.randint(100, 999)}-"
                f"{random.randint(10, 99)}-"
                f"{random.randint(10, 99)}"
            )
            email = (
                f"{first_name.lower()}."
                f"{last_name.lower()}@"
                f"{random.choice(domains)}"
            )
            advertising_company = random.choice(advertising_companies)

            client, create = Client.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                phone_number=phone_number,
                email=email,
                advertising_company=advertising_company,
                next_interaction_date=self.random_date(),
            )

            self.stdout.write(
                f"Created client: {client.first_name} {client.last_name}"
            )

        self.stdout.write(self.style.SUCCESS("Clients created"))
