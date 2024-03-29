from django.db import models
from eshop.utils import upload_image_path


class Setting(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان سایت")
    address = models.CharField(max_length=50, verbose_name="ادرس")
    phone = models.CharField(max_length=50, verbose_name="تلفن ")
    mobile = models.CharField(max_length=50, verbose_name="تلفن همراه")
    email = models.EmailField(max_length=50, verbose_name="ایمیل")
    copyright = models.CharField(max_length=50, verbose_name="کپی رایت")
    about_us = models.TextField(verbose_name="درباره سایت")
    logo = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر لکو سایت', default=None, null=True)

    # todo:add image field for logo
    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "مدیریت تنظیمات سایت"

    def __str__(self):
        return self.title
