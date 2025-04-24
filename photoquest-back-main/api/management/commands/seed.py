from django.core.management.base import BaseCommand
from api.models import Category, Quest

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Quest.objects.all().delete()

        nature = Category.objects.create(name="Nature")
        city = Category.objects.create(name="City")

        Quest.objects.create(title="Sunset at the river", description="Take a photo of the sunset near water", difficulty="easy", category=nature)
        Quest.objects.create(title="Street musician", description="Find a street musician and take a photo", difficulty="medium", category=city)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
