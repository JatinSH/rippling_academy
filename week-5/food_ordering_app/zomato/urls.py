from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('restaurant_list/', views.restaurant_list, name="restaurant_list"),
    path('restaurant_detail/<str:pk>/', views.restaurant_detail, name="restaurant_detail"),
    path('add_restaurant/', views.add_restaurant, name="add_restaurant"),
    path('delete_restaurant/<str:pk>/', views.delete_restaurant, name="delete_restaurant"),
    # path('select_delete_restaurant', views.select_delete_restaurant, name="select_delete_restaurant"),
    # path('select_manage_restaurant', views.select_manage_restaurant, name="manage_restaurant"),
    # path('manage_restaurant', views.manage_restaurant, name="manage_restaurant"),
    # path('order', views.order, name="order"),
]
