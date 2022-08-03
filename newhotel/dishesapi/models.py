from django.db import models

# Create your models here.
class Dishes(models.Model):
    dish=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    rating=models.FloatField()
    def __str__(self):
        return self.dish


# Dishes.objects.create(dish="veg biriyani",category="veg",price=120,rating=4)