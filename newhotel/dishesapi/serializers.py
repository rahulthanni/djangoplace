from rest_framework import serializers
from dishesapi.models import Dishes
from django.contrib.auth.models import User

class DishesSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    dish=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

    def validate(self, data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("Invalid data")
        return data

class DishesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]