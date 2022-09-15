from django.shortcuts import render
from . models import Product

def index(request):
    stat = Product.objects.all()
    return render(request , 'main/index.html', {'stat':stat})

def base(request):
    render(request, "main/base.html")