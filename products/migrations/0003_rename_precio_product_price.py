# Generated by Django 3.2.9 on 2022-04-19 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
    ]