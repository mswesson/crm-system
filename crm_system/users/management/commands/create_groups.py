from django.core.management import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Creates groups"""

    def handle(self, *args, **options):
        groups_names = ["administrator", "operator", "marketer", "manager"]

        for group_name in groups_names:
            group, created = Group.objects.get_or_create(name=group_name)
            self.stdout.write(f"Created group {group.name}")

        self.stdout.write(self.style.SUCCESS("Groups created"))
