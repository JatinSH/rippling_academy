from rest_framework_mongoengine import serializers
from .models import Restaurant, FoodItems


class RestaurantSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodItemsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = FoodItems
        fields = '__all__'

