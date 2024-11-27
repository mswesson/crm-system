from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Запускает несколько команд для создания объектов"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Executing the command create_groups...")
        call_command("create_groups")

        self.stdout.write("Executing the command create_users...")
        call_command("create_users")

        self.stdout.write("Executing the command create_services...")
        call_command("create_services")

        self.stdout.write("Executing the command create_advertising...")
        call_command("create_advertising")

        self.stdout.write("Executing the command create_clients...")
        call_command("create_clients")

        self.stdout.write("Executing the command create_contracts...")
        call_command("create_contracts")

        self.stdout.write(
            self.style.SUCCESS("All commands completed successfully!")
        )
