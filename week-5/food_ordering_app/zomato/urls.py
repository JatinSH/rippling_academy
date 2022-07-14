from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add_restaurant', views.add_restaurant, name="add_restaurant"),
    path('delete_restaurant', views.delete_restaurant, name="delete_restaurant"),
    path('manage_restaurant', views.manage_restaurant, name="manage_restaurant"),
    path('order', views.order, name="order"),
]
