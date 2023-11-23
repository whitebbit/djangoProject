from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Blog

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of blogs to be created"
        )

    def handle(self, *args, **options):
        total = options["total"]
        Blog.objects.all().delete()

        for _ in range(total):
            Blog.objects.create(
                title=fake.sentence(),
                content=fake.paragraphs(),
                updated_at=fake.date_time_this_decade(),
            )
