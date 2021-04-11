# import string
from django.db import models
from django.db.models import Q
from eshop_products_category.models import ProductsCategory
from eshop.utils import upload_image_path, get_file_name
from django.contrib.auth.models import User


# import os
# import random


# from django.

# def get_file_name(filepath):
#     size = 8
#     chars = string.ascii_uppercase + string.digits
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     name = ''.join(random.choice(chars) for _ in range(size))
#     print(name)
#     return name, ext


# def upload_image_path(instance, filename):
#     name, ext = get_file_name(filename)
#     new_name = f"{name}{ext}"
#     return f"product/{instance.title}/{new_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_categories(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)

    def get_product_by_id(self, productid):
        qs = self.get_queryset().filter(id=productid, active=True)

        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):

        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان محصول')
    # english_title = models.SlugField(max_length=150, verbose_name='عنوان انگلیسی', default='-')
    description = models.TextField(verbose_name='توضیحات محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                              verbose_name='تصویر محصول')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    objects = ProductManager()
    category = models.ManyToManyField(ProductsCategory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def __str__(self):
        return self.title


def upload_gallery_image_path(instance, filename):
    name, ext = get_file_name(filename)
    new_name = f"{instance.id}-{name}{ext}"

    return f"product/gallery/{new_name}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان تصویر")
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر محصول')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="انتخاب محصول")

    class Meta:
        verbose_name_plural = 'گالری ها'
        verbose_name = 'گالری'

    def __str__(self):
        return self.title


class UserComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول مربوطه")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر مربوطه")
    title = models.CharField(max_length=150, verbose_name="عنوان دیدگاه")
    text = models.TextField(verbose_name="متن دیدگاه کاربر")
    date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد دیدگاه")

    class Meta:
        verbose_name_plural = "دیدگاه"
        verbose_name = "دیدگاه"

    def __str__(self):
        return self.title
