from django.core.management import BaseCommand

from clients.models import Client


class Command(BaseCommand):
    """Удаляет клиентов"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete clients")
        clients = Client.objects.all()
        clients.delete()
        self.stdout.write(self.style.SUCCESS("Clients deleted"))
