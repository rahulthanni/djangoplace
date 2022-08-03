from django.db import models

# Create your models here.
class DishDetails(models.Model):
    dish=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()
    def __str__(self):
        return self.dish
