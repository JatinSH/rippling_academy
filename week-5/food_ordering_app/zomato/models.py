from django.db import models
from mongoengine import *


# Create your models here.
class Restaurant(Document):
    restaurant_name = StringField(required=True)
    restaurant_address = StringField()
    restaurant_cuisines = ListField(StringField())

