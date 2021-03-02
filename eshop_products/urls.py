from django.urls import path
from .views import ProductsList, product_detail, ProductSearch, product_categories_partial, ProductsListByCategory

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),

    path('products/search', ProductSearch.as_view()),
    path('products/<productid>/<category_name>', product_detail),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial'),
]
