from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from zomato.models import Restaurant
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer


# Create your views here.


# def home(request):
#     return render(request, 'home.html', {'name': 'jatin'})

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
    print(request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_restaurant(request, pk):
    restaurant = Restaurant.objects(id=pk)[0]
    restaurant.delete()
    return  Response("Restaurant Deleted!")
# def add_restaurant(request):
#     if request.method == "GET":
#         return render(request, 'add_restaurant.html')
#     else:
#         restaurant = Restaurant()
#         restaurant.restaurant_name = request.POST['restaurant_name']
#         restaurant.restaurant_address = request.POST['restaurant_address']
#         restaurant.restaurant_cuisines = request.POST.getlist('cuisines')
#         restaurant.save()
#         return redirect('/')
#
#
# def select_delete_restaurant(request):
#     if request.method == "GET":
#         return render(request, 'select_delete_restaurant.html')
#     else:
#         restaurant_name = request.POST['restaurant_name']
#         restaurants = Restaurant.objects(restaurant_name__contains=restaurant_name)
#         return render(request, 'select_delete_restaurant.html', {"restaurants": restaurants})
#
#
# def delete_restaurant(request):
#     restaurant_id = request.POST['restaurant.id']
#     restaurant_to_delete = Restaurant.objects(id=restaurant_id)
#     restaurant_to_delete.delete()
#     return HttpResponse("Restaurant Deleted!!")
#
#
# def select_manage_restaurant(request):
#     if request.method == "GET":
#         return render(request, 'select_manage_restaurant.html')
#     else:
#         restaurant_name = request.POST['restaurant_name']
#         restaurants = Restaurant.objects(restaurant_name__contains=restaurant_name)
#         return render(request, 'select_manage_restaurant.html', {"restaurants": restaurants})
#
#
# def manage_restaurant(request):
#     restaurant_id = request.POST['restaurant.id']
#     restaurant_to_manage = Restaurant.objects(id=restaurant_id)
#
#
# def order(request):
#     return render(request, 'order.html')
