# Generated by Django 3.1.2 on 2021-03-03 15:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0012_auto_20210303_1813'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_account', '0003_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Favorite',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='department',
            new_name='favorite_product',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='favorite_product',
            field=models.ManyToManyField(blank=True, null=True, to='eshop_products.Product'),
        ),
    ]