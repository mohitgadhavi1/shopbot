from django.db import models

# Create your models here.from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    original_price = models.FloatField()
    image = models.URLField()
    rating = models.FloatField()
    reviews = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
