from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from eshop_order.forms import UserNewOrderForm
from eshop_order.models import Order
from eshop_products.models import Product


@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count <= 0:
            count = 1
        product = Product.objects.get_product_by_id(productid=product_id)
        order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)

    return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None,
        'title': 'سبد خرید | فروشگاه آزمایشی'

    }

    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
    return render(request, 'order/user_open_order.html', context)
