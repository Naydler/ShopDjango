from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from .models import product

# Create your views here.


def get_all_products(request):
    products = product.objects
    product_list = products.values_list('name', flat=True)
    product_names = '\n'.join(product_list)
    return HttpResponse(product_names)

def get_all_products_by_category(request, categorysearch):
    products = product.objects.filter(category = categorysearch)
    product_list = products.values_list('name', flat=True)
    product_names = '\n'.join(product_list)
    return HttpResponse(product_names)

def get_all_products_by_size(request, sizesearch):
    # Validamos que el tamaño sea un solo carácter
    if len(sizesearch) != 1:
        return HttpResponseBadRequest('Size search must be a single character.')
    
    # Filtrar productos por tamaño
    products = product.objects.filter(size=sizesearch)
    
    product_list = products.values_list('name', flat=True)
    product_names = '\n'.join(product_list)
    return HttpResponse(product_names)

def get_all_products_by_price(request, pricesearch):
    products = product.objects.filter(price__gt=pricesearch).values('name', 'price')
    product_list = [f"{product['name']} - {product['price']}" for product in products]
    product_names = '\n'.join(product_list)
    return HttpResponse(product_names)


def product_list(request):
    products = product.objects.all()
    return render(request, 'products/products_list.html' , {'products': products})

def update_product(request, id):
    products = product.objects.filter('id' == id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        size = request.POST.get('size')
        
        products.name = name
        products.price = price
        products.category = category
        products.size = size
        products.save()
        return render(request, 'products/products_list.html' , {'products': products})
    
    return redirect(request, 'products/update_products.html' , {'products': products})


    
