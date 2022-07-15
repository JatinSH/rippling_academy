from mongoengine import Q

from zomato.models import Restaurant, FoodItems, Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer, FoodItemsSerializer, OrderSerializer


@api_view(['GET'])
def home(request):
    return Response({})


@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects(id=pk)[0]
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_restaurant(request, pk):
    restaurant = Restaurant.objects(id=pk)[0]
    restaurant.delete()
    return Response("Restaurant Deleted!")


@api_view(['GET'])
def menu(request):
    food_items = FoodItems.objects
    serializer = FoodItemsSerializer(food_items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_restaurant_menu(request):
    serializer = FoodItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update_restaurant_menu(request, pk, pk2):
    restaurant = Restaurant.objects(id=pk)[0]
    food_item = FoodItems.objects(Q(restaurant=restaurant) & Q(id=pk2))[0]

    serializer = FoodItemsSerializer(instance=food_item, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def filter_menu_by_cuisine(request, cuisine):
    food_items = FoodItems.objects(cuisine__icontains=cuisine)
    serializer = FoodItemsSerializer(food_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_menu_by_restaurant(request, pk):
    food_items = FoodItems.objects(restaurant=pk)
    serializer = FoodItemsSerializer(food_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_menu_by_name(request, name):
    print(name)
    food_items = FoodItems.objects(name__icontains=name)
    serializer = FoodItemsSerializer(food_items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        all_orders = Order.objects
        serializer = OrderSerializer(all_orders, many=True)
        return Response(serializer.data)
    else:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
