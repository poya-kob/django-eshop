# Generated by Django 3.1.2 on 2021-03-03 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account', '0006_auto_20210303_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='curent_user_id',
            new_name='current_user_id',
        ),
    ]
