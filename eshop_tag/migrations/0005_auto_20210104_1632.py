# Generated by Django 3.1.2 on 2021-01-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_product_category'),
        ('eshop_tag', '0004_auto_20201113_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
    ]
