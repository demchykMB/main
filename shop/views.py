from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login


def index(request):
    stat = Product.objects.all()
    return render(request, 'HTML/index.html', {'stat': stat})



