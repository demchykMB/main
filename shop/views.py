from django.shortcuts import render
from . models import Product


def index(request):
    stat = Product.objects.all()
    return render(request , 'HTML/index.html', {'stat': stat})

def lest1(request):
    context = {}
    return render(request, "HTML/product.html", context)