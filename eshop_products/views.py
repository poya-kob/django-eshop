import itertools
from .forms import CommentForm
from django.shortcuts import render
from django.views.generic import ListView
from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery, UserComment
from django.http import Http404
from eshop_products_category.models import ProductsCategory
from eshop_account.models import Favorite
from django.core.paginator import Paginator


# Create your views here.
class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.get_active_products()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        user_favorite_list = Favorite.objects.values_list('favorite_product').filter(
            current_user_id__exact=self.request.user.id)
        user_favorite_product = []
        for Tuple in list(user_favorite_list):
            user_favorite_product.append(Tuple[0])
        context['favorite_list'] = user_favorite_product
        context['title'] = 'لیست محصولات | فروشگاه آزمایشی'
        return context


# def products_list(request):
#     product = Product.objects.get_active_products()
#     user_favorite_list = Favorite.objects.values_list('favorite_product').filter(
#         current_user_id__exact=request.user.id)
#
#     paginate_by = 4


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
    user_favorite_list = Favorite.objects.filter(current_user_id__exact=request.user.id,
                                                 favorite_product__exact=selected_product_id).exists()
    # comment part
    user_commented = UserComment.objects.filter(active=True, user_id=request.user.id,
                                                product_id=selected_product_id).__bool__()
    user_comments = UserComment.objects.order_by('-id').filter(active=True, product_id=selected_product_id)
    comment_form = CommentForm(request.POST or None)
    if request.user.is_authenticated and not user_commented:
        if comment_form.is_valid():
            UserComment.objects.create(user_id=request.user.id, product_id=selected_product_id,
                                       title=comment_form.cleaned_data.get('title'),
                                       text=comment_form.cleaned_data.get('text'))
    total_comments = UserComment.objects.filter(active=True, product_id=selected_product_id).count()
    paginator = Paginator(user_comments, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # comment part
    # print(user_favorite_list)
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
        'new_order_form': new_order_form,
        'favorite_list': user_favorite_list,
        'comment_form': comment_form,
        'user_comments': user_comments,
        'total_comments': total_comments,
        'user_commented': user_commented,
        'paginator': page_obj,
        'paginator_range': paginator.page_range,
        'title': 'جزئیات محصول | فروشگاه آزمایشی '
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
