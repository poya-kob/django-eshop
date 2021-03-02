from django.core.exceptions import ValidationError
# from eshop_products.models import get_file_name
from eshop.utils import upload_image_path
from django.db import models

from eshop_products.models import Product


# def get_file_name(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_image_path(instance, filename):
#     name, ext = get_file_name(filename)
#     new_name = f"{name}{ext}"
#
#     return f"slider/{instance.english_title}/{new_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان", null=True, blank=True)
    # english_title = models.SlugField(max_length=150, verbose_name='عنوان انگلیسی', null=True, blank=True, default='-')
    link = models.URLField(max_length=100, verbose_name="آدرس", null=bool(title), blank=bool(title))
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True,
                              blank=True, verbose_name='تصویر اسلایدر')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True, unique=True,
                                   verbose_name="محصول")

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"

    def __str__(self):
        if self.title is not None:
            return self.title
        else:
            return self.product.title

    def clean(self):
        slider_count = Slider.objects.count()

        if slider_count >= 4:
            raise ValidationError("تعداد اسلایدر ها نمیتاند بیشتر از 4 اسلایدر باشد")
