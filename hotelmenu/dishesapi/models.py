from django.db import models

# Create your models here.
class Dishes(models.Model):
    dish_name=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()
    def __str__(self):
        return self.dish_name
