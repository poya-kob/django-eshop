# Generated by Django 3.1.2 on 2021-03-10 13:14

import ckeditor_uploader.fields
from django.db import migrations, models
import eshop.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان مطلب')),
                ('image', models.ImageField(upload_to=eshop.utils.upload_image_path, verbose_name='بنر خبر -398*862-')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد پست')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن خبر')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]
