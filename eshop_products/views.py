import itertools

from django.shortcuts import render
from django.views.generic import ListView

from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from django.http import Http404
from eshop_products_category.models import ProductsCategory

from eshop_account.models import Favorite


# Create your views here.
class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductsCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_products_by_categories(category_name)


def gallery_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productid']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    #
    Favorite.objects.create(favorite_product=selected_product_id, current_user_id=request.user.id)
    #
    got_product: Product = Product.objects.get_product_by_id(selected_product_id)
    got_product.visit_count += 1
    got_product.save()
    # print(got_product.active)
    if got_product is None or not got_product.active:
        raise Http404('محصول مورد نظر یافت نشد.')

    related_product = Product.objects.get_queryset().filter(category__product=got_product, active=True).distinct()
    grouped_related_product = list(gallery_grouper(3, related_product))
    # print(grouped_related_product)
    galleries = ProductGallery.objects.filter(product_id=selected_product_id)
    grouped_gallery = list(gallery_grouper(3, galleries))

    context = {
        'object': got_product,
        'gallery': grouped_gallery,
        'related_product': grouped_related_product,
        'new_order_form': new_order_form
    }

    return render(request, 'products/product_detail.html', context)


class ProductSearch(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        return Product.objects.search(query)


def product_categories_partial(request):
    category = ProductsCategory.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'products/product_categories_partial.html', context)
