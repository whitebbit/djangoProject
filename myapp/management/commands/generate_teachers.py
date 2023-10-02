import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from myapp.models import Teacher


class Command(BaseCommand):
    help = "Generate random teachers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=100, help="Number of teachers to generate"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        fake = Faker()
        for _ in range(count):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date(),
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully generated teacher"))
