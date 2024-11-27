from django.core.management import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):
    """Удаляет пользователей"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete users")
        users = User.objects.all()
        users.delete()
        self.stdout.write(self.style.SUCCESS("Users deleted"))
