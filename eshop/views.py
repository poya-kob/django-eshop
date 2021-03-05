from django.shortcuts import render
from eshop_sliders.models import Slider
from eshop_setting.models import Setting
from eshop_products.models import Product
from eshop_products.views import gallery_grouper


def header(request, *args, **kwargs):
    context = {
        'title': 'new title'
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    setting = Setting.objects.last()
    context = {
        'setting': setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    slider = Slider.objects.all()
    most_visited_products = Product.objects.order_by('-visit_count').filter(active=True)[:8]
    last_products = Product.objects.order_by('-id').filter(active=True)[:8]

    context = {
        "sliders": slider,
        "most_visited_products": gallery_grouper(4, most_visited_products),
        "last_products": gallery_grouper(4, last_products),

    }
    return render(request, "home_page.html", context)


def about_page(request):
    setting: Setting = Setting.objects.last()
    context = {
        'setting': setting
    }
    return render(request, 'about_page.html', context)
