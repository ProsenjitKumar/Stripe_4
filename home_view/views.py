from django.shortcuts import render
from product.models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    template = 'home.html'
    return render(request, template, context)