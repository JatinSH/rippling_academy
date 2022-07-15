from django.db import models
from mongoengine import *


# Create your models here.
class Restaurant(Document):
    restaurant_name = StringField(required=True)
    restaurant_address = StringField()
    restaurant_cuisines = ListField(StringField())
    restaurant_logo = StringField()


class FoodItems(Document):
    name = StringField(required=True)
    description = StringField()
    image = StringField()
    veg = BooleanField()
    quantity = IntField()
    cuisine = StringField()
    available = StringField()
    price = FloatField()
    restaurant = ReferenceField(Restaurant, reverse_delete_rule=CASCADE)


class Order(Document):
    item = ReferenceField(FoodItems)