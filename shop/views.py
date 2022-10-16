from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login



def index(request):
    stat = Product.objects.all()
    return render(request, 'HTML/index.html', {'stat': stat})


def shop(request):

    return render(request, 'HTML/shop.html')



