from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مالک سبد")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده / نشده")
    payment_date = models.DateTimeField(verbose_name='زمان پزداخت', blank=True, null=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.owner.get_full_name()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name="قیمت محصول")
    count = models.IntegerField(default=1, verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'

    def __str__(self):
        return self.product.title
