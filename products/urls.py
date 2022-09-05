from django.urls import path
from products.views import products_index, products_home ,products_list
urlpatterns = [
    path("all", products_index),
    path("home", products_home),
    path("list", products_list)

]
