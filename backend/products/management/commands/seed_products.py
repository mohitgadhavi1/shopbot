from django.core.management.base import BaseCommand
from products.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with 100 mock products'

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ['Electronics', 'Books', 'Clothing', 'Home', 'Toys']

        Product.objects.all().delete()  # Optional: Clear old data

        for i in range(100):
            name = fake.catch_phrase()
            price = round(random.uniform(10, 999), 2)
            original_price = price + round(random.uniform(5, 100), 2)
            image = f"https://source.unsplash.com/400x400/?product,{i}"
            rating = round(random.uniform(3, 5), 1)
            reviews = random.randint(10, 5000)
            category = random.choice(categories)
            description = fake.sentence(nb_words=12)

            Product.objects.create(
                name=name,
                price=price,
                original_price=original_price,
                image=image,
                rating=rating,
                reviews=reviews,
                category=category,
                description=description
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded 100 products.'))
