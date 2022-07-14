from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from zomato.models import Restaurant


# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'jatin'})


def add_restaurant(request):
    if request.method == "GET":
        return render(request, 'add_restaurant.html')
    else:
        restaurant = Restaurant()
        restaurant.restaurant_name = request.POST['restaurant_name']
        restaurant.restaurant_address = request.POST['restaurant_address']
        restaurant.restaurant_cuisines = request.POST.getlist('cuisines')
        restaurant.save()
        return redirect('/')


def delete_restaurant(request):
    if request.method == "GET":
        return render(request, 'delete_restaurant.html')
    else:
        restaurant_name = request.POST['restaurant_name']
        restaurants = Restaurant.objects(restaurant_name__contains=restaurant_name)
        return render(request, 'delete_restaurant.html', {"restaurants": restaurants})


def manage_restaurant(request):
    return render(request, 'manage_restaurant.html')


def order(request):
    return render(request, 'order.html')
