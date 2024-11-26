from django.core.management import BaseCommand
from django.contrib.auth.models import User, Group
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """Creates users"""

    def add_group(self, user: User, group_name: str):
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            self.stdout.write(f"The group {group_name} not found")
            return

        user.groups.add(group)
        user.save()

        self.stdout.write(
            f"The user {user.username} has been "
            f"added to the group {group_name}"
        )

    def handle(self, *args, **options):
        self.stdout.write("Create users")

        users_data = [
            {
                "username": "themswesson",
                "first_name": "Eduard",
                "last_name": "Komarov",
                "email": "rango.adik@gmail.com",
                "password": "123456Ww",
                "group_name": "administrator",
                "is_superuser": True,
                "is_staff": True,
            },
            {
                "username": "mikel",
                "first_name": "Mikhail",
                "last_name": "Kravets",
                "email": "mikel@gmail.com",
                "password": "123456Ww",
                "group_name": "operator",
                "is_superuser": False,
                "is_staff": False,
            },
            {
                "username": "lipton",
                "first_name": "Alexey",
                "last_name": "Sizykh",
                "email": "lipton@gmail.com",
                "password": "123456Ww",
                "group_name": "marketer",
                "is_superuser": False,
                "is_staff": False,
            },
            {
                "username": "hetekwa",
                "first_name": "Taya",
                "last_name": "Legkova",
                "email": "hetewka@gmail.com",
                "password": "123456Ww",
                "group_name": "manager",
                "is_superuser": False,
                "is_staff": False,
            },
        ]

        for user_data in users_data:
            try:
                user = User.objects.create_user(
                    username=user_data["username"],
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    email=user_data["email"],
                    password=user_data["password"],
                    is_superuser=user_data["is_superuser"],
                    is_staff=user_data["is_staff"],
                )

                self.stdout.write(f"User {user.username} create")

            except IntegrityError:
                self.stdout.write(
                    f"User {user_data["username"]} alredy exists"
                )
                user = User.objects.get(username=user_data["username"])

            self.add_group(user=user, group_name=user_data["group_name"])

        self.stdout.write(self.style.SUCCESS("Products created"))
