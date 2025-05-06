from django.shortcuts import render
from .models import Product

def product_list(request):
    macs = Product.objects.filter(category__iexact='Mac')
    iphones = Product.objects.filter(category__iexact='iPhone')

    watches = Product.objects.filter(category__iexact='Watch')
    ipads = Product.objects.filter(category__iexact='Ipad')

    context = {
        'macs': macs,
        'iphones':iphones,
        'watches': watches,
        'ipads': ipads,
    }
    return render(request, 'apple/apple_home.html', context)

