# Generated by Django 4.2.2 on 2023-07-13 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_delete_productgallery'),
        ('cart', '0005_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('product', 'cart')},
        ),
    ]