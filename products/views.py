from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products" : products})


def details(request, id):
    product = Product.objects.get(id = id)
    return render(request, "single.html", {"product" : product})