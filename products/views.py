import os

from django.shortcuts import render, redirect, get_object_or_404

from products.form import ProductForm
from products.models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # print("Form valid?", form.is_valid())
        # print("Form errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/products/list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form_create.html', {'form': form})


def product_edit(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/products/list')
    return render(request, 'products/product_form_edit.html', {'form': form, 'product': product})


def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        if product.image and os.path.isfile(product.image.path):
            os.remove(product.image.path)
        product.delete()
        return redirect('/products/list')
    return redirect('/products/list')
