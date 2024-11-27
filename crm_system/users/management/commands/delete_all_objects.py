from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Запускает несколько команд для удаления объектов"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Executing the command delete_contracts...")
        call_command("delete_contracts")

        self.stdout.write("Executing the command delete_clients...")
        call_command("delete_clients")

        self.stdout.write("Executing the command delete_advertising...")
        call_command("delete_advertising")

        self.stdout.write("Executing the command delete_services...")
        call_command("delete_services")

        self.stdout.write("Executing the command delete_users...")
        call_command("delete_users")

        self.stdout.write("Executing the command delete_groups...")
        call_command("delete_groups")

        self.stdout.write(
            self.style.SUCCESS("All commands completed successfully!")
        )
