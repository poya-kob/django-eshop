# Generated by Django 3.1.2 on 2021-01-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_productgallery'),
        ('eshop_tag', '0006_auto_20210106_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
    ]
