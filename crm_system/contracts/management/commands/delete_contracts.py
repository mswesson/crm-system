from django.core.management import BaseCommand

from contracts.models import Contract


class Command(BaseCommand):
    """Удаляет контракты"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete contracts")
        contracts = Contract.objects.all()
        contracts.delete()
        self.stdout.write(self.style.SUCCESS("Contracts deleted"))
