from django.core.management import BaseCommand

from advertising.models import AdvertisingCompany


class Command(BaseCommand):
    """Удаляет рекламные компании"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete advertising")
        advertising = AdvertisingCompany.objects.all()
        advertising.delete()
        self.stdout.write(self.style.SUCCESS("Advertising deleted"))
