from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Cписок продуктов'
    }
    return render(request, 'catalog/index.html', context)

def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item
    }
    return render(request, 'catalog/product.html', context)

def contacts(request):
    return render(request, 'catalog/index2.html')
