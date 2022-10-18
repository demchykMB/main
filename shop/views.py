from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView
from django.http import FileResponse


class NewsDatailView(DetailView):
    model = Product
    template_name = 'HTML/shop.html'
    context_object_name = 'products'

    def image_product(self, context, **kwargs):
        return FileResponse(self.object.image)


def index(request):
    stat = Product.objects.all()
    return render(request, 'HTML/index.html', {'stat': stat})


def shop(request):
    produk = Product.objects.all()
    return render(request, 'HTML/shop.html', {'produk': produk})



