from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from eshop.utils import upload_image_path


# from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان مطلب")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="بنر خبر -398*862-")
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد پست")
    description = models.TextField(max_length=690, verbose_name="توضیحات کوتاه(یک پاراگراف)")
    text = RichTextUploadingField(verbose_name="متن خبر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "اخبار"
        verbose_name = "خبر"
