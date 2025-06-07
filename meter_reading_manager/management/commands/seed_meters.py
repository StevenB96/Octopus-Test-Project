from django.core.management.base import BaseCommand
from meter_reading_manager.models import Meter
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with fake Meter data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):
            Meter.objects.create(
                name=fake.name(),
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded 50 Meter records.'))
