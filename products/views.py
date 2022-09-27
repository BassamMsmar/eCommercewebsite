from django.shortcuts import render
from django.core.paginator import Paginator

from .models import*

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

def products(request):
    product = Product.objects.all()
    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products':paged_products,
        
    }
    return render(request, 'products/products.html', context)