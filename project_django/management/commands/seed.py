from django.core.management import BaseCommand
from django.contrib.auth.models import User
from todolist.models import Task
import string
import random

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for production."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options) -> None:
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    print("Delete Tasks instances")
    User.objects.all().delete()
    Task.objects.all().delete()


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """

    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # seeding db
    create_super_user()
    create_task()


def create_super_user():
    User.objects.create_superuser(
        username="admin", email="admin@gmail.com", password="3231"
    )


def random_string(n=20) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def create_task():
    """Creates an task object combining different elements from the list"""
    print("Creating tasks")
    USER_DATA = [
        {
            "username": "dummyuser1",
            "password": "dummypassword1",
        },
        {
            "username": "dummyuser2",
            "password": "dummypassword2",
        },
    ]

    for i in range(2):
        User.objects.create_user(**USER_DATA[i])

    user1 = User.objects.all()[1]
    user2 = User.objects.last()

    for _ in range(3):
        Task.objects.create(
            user=user1, title="User1 " + random_string(), description=random_string()
        )

    for _ in range(3):
        Task.objects.create(
            user=user2, title="User2 " + random_string(), description=random_string()
        )

    print(f"tasks created.")
