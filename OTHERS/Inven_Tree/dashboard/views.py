from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from sqlalchemy import null
from .model import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
import pandas as pd
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(product='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('product')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }

    df = pd.read_csv('media/BigBasket Products.csv')
    lst = []
    for i in range(len(df)):
        lst.append(df.iloc[i])

    for column in lst:
        _, created = Product.objects.update_or_create(
            product = column[1],
            category = column[2],
            sub_category = column[3],
            brand = column[4],
            sale_price = column[5],
            market_price = column[6],
            product_type = column[7],
            rating = column[8],
            description = column[9],
            total_quantity = column[10],
        )

    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('product')
            product_quantity = form.cleaned_data.get('order_quantity')
            bought_product = Product.objects.get(product=product_name)
            bought_product.total_quantity -= product_quantity
            if bought_product.total_quantity >= 0:
                messages.success(request, 'Order has been added')
                Product.objects.filter(product=product_name).update(total_quantity=bought_product.total_quantity)
                return redirect('dashboard-order')
            else:
                messages.error(request,'Product Unavailable')
                Order.objects.filter(order_quantity = product_quantity).delete()
                return redirect('dashboard-order')
    else:
        form = OrderForm()

    context = {
        'order': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
        'form': form
    }

    return render(request, 'dashboard/order.html', context)
