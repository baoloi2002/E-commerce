# Generated by Django 5.0.3 on 2024-04-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='review',
        ),
    ]
