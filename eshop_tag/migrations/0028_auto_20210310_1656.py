# Generated by Django 3.1.2 on 2021-03-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0012_auto_20210303_1813'),
        ('eshop_tag', '0027_auto_20210310_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
    ]
