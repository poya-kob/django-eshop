# Generated by Django 3.1.2 on 2021-03-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_blog', '0002_blog_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=2, max_length=690, verbose_name='توضیحات کوتاه(یک پاراگراف)'),
            preserve_default=False,
        ),
    ]