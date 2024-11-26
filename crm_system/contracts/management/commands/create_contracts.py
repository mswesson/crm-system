from django.core.management import BaseCommand
import random
from django.utils import timezone
from datetime import datetime, timedelta

from clients.models import Client
from contracts.models import Contract


class Command(BaseCommand):
    """Создает контракты и переводит клиентов в активных"""

    def random_date(self) -> datetime:
        """Рандомная дата в пределах 15-360 дней только в будущее"""
        now = timezone.now()
        delta = timedelta(days=360)
        random_offset = random.uniform(1_296_000, delta.total_seconds())
        result_data = now + timedelta(seconds=random_offset)
        return result_data

    def handle(self, *args, **options):
        self.stdout.write("Start creating contracts")

        potential_clients = list(Client.objects.filter(is_active=False))
        if not potential_clients:
            self.stdout.write("The advertising were not created in advance")
            return

        for _ in range(30):
            end_date_contract = self.random_date()
            
            #  Client
            client = potential_clients.pop(
                random.randint(0, len(potential_clients) - 1)
            )
            client.next_interaction_date = end_date_contract
            client.is_active = True
            client.notes += (
                "\n- The contract has been signed. "
                f"End date {end_date_contract}"
            )
            client.save()

            #  Service
            service = client.advertising_company.service
            budget = service.price

            #  Contract
            title = (
                f"#{random.randint(0, 10000)} "
                f"{client.last_name[:1]}. {client.first_name} "
                f"- {service.title}"
            )

            contract = Contract(
                title=title,
                service=service,
                client=client,
                end_date=end_date_contract,
                budget=budget,
            )
            contract.save()

            self.stdout.write(f"Created contract: {title}")

        self.stdout.write(self.style.SUCCESS("Contracts created"))
