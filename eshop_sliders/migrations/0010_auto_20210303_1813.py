# Generated by Django 3.1.2 on 2021-03-03 14:43

from django.db import migrations, models
import eshop.utils


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0009_auto_20210220_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=eshop.utils.upload_image_path, verbose_name='تصویر اسلایدر'),
        ),
    ]