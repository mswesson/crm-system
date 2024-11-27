from django.core.management import BaseCommand

from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Удаляет группы"""

    def handle(self, *args, **options):
        self.stdout.write("Start delete groups")
        groups = Group.objects.all()
        groups.delete()
        self.stdout.write(self.style.SUCCESS("Groups deleted"))
