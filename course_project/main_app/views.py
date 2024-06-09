from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            if 'product_count' in request.session:
                request.session['product_count'] += 1
            else:
                request.session['product_count'] = 1
            return redirect('product_count')
    else:
        form = ProductForm()

    return render(request, 'myapp/add_product.html', {'form': form})


def product_count(request):
    count = request.session.get('product_count', 0)
    return render(request, 'myapp/product_count.html', {'count': count})