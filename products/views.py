from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def products_index(request):
    return HttpResponse("this my products index")

def products_list(request):
    allProducts=[
        {'id': 1, 'name': 'product1', 'image': 'product1.png'},
        {'id': 2, 'name': 'product2', 'image': 'product2.png'},
        {'id': 1, 'name': 'product3', 'image': 'product3.png'}
    ]
    return render(request, "products/productsall.html", context={'products': allProducts})

def products_home(request):
    return render(request,"products/home.html")