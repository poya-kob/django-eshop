# Generated by Django 3.1.2 on 2021-01-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_productgallery'),
        ('eshop_tag', '0008_auto_20210111_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
    ]
