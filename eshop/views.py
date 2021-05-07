from django.shortcuts import render
from eshop_sliders.models import Slider
from eshop_setting.models import Setting
from eshop_products.models import Product
from eshop_products.views import gallery_grouper
from eshop_account.models import Favorite


def header(request, *args, **kwargs):
    setting = Setting.objects.last()
    context = {
        'title': 'new title',
        'setting': setting
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    setting = Setting.objects.last()
    context = {
        'setting': setting
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    a = 15
    slider = Slider.objects.all()
    most_visited_products = Product.objects.order_by('-visit_count').filter(active=True)[:8]
    last_products = Product.objects.order_by('-id').filter(active=True)[:8]
    user_favorite_list = Favorite.objects.values_list('favorite_product').filter(
        current_user_id__exact=request.user.id)
    user_favorite_product = []
    for Tuple in list(user_favorite_list):
        user_favorite_product.append(Tuple[0])
    # print(user_favorite_product)
    # if a in user_favorite_product:
    #     print('yes')
    context = {
        "sliders": slider,
        "most_visited_products": gallery_grouper(4, most_visited_products),
        "last_products": gallery_grouper(4, last_products),
        "favorite_list": user_favorite_product,
        "title": "صفحه اصلی | فروشگاه آزمایشی"

    }
    return render(request, "home_page.html", context)


def about_page(request):
    setting: Setting = Setting.objects.last()
    context = {
        'setting': setting,
        'title': 'درباره ما | فروشگاه آزمایشی'
    }
    return render(request, 'about_page.html', context)
