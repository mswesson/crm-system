from django.core.management import BaseCommand

from services.models import Service


class Command(BaseCommand):
    """Удаляет услуги"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete services")
        services = Service.objects.all()
        services.delete()
        self.stdout.write(self.style.SUCCESS("Services deleted"))
