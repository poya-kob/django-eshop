# Generated by Django 3.1.2 on 2020-11-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0003_auto_20201110_1908'),
        ('eshop_tag', '0002_tag_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'تگ/برچسب', 'verbose_name_plural': 'تگ ها / برچسب ها'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]
