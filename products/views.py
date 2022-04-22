from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def home(request):
    products = Product.objects.all()
    all_products = []
    for product in products:
      all_products.append({"name" : product.name, 
                        "price" : product.price,
                        "id" : product.id,
                        "image" : product.image,
                        "description" : product.description,
                        "offert" : product.offert,
                        "bio" : product.bio})
    if request.is_ajax():
      return JsonResponse({"data" : all_products})
    return render(request, "index.html")


def details(request, id):
    product = Product.objects.get(id = id)
    return render(request, "single.html", {"product" : product})
    

def load(request):
  products = Product.objects.all()[2:]
  all_products = []
  for product in products:
    all_products.append({"name" : product.name, 
                        "price" : product.price,
                        "id" : product.id,
                        "image" : product.image,
                        "description" : product.description,
                        "offert" : product.offert,
                        "bio" : product.bio,
    })
  if request.is_ajax():
    return JsonResponse({"lasts" : all_products})
  return render(request, "index.html")



def privacy_policy(request):
  return render(request, "privacy.html")

def terms(request):
  return render(request, "terms.html")

def helpme(request):
  return render(request, "help.html")

def contact(request):
  return render(request, "contact.html")

def faqs(request):
  return render(request, "faqs.html")

def payment(request):
  return render(request, "payment.html")


def about(request):
  return render(request, "about.html")
  
def checkout(request):
  products = Product.objects.all()
  cart_products = []
  for product in products:
    cart_products.append({"name" : product.name, 
                        "price" : product.price,
                        "id" : product.id,
                        "image" : product.image,
                        "description" : product.description,
                        "offert" : product.offert,
                        "bio" : product.bio,
                        "quantity" : 1,
    })
  if request.is_ajax():
    return JsonResponse({"list" : cart_products})
  return render(request, "checkout.html")