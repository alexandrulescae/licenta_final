# Generated by Django 4.0.3 on 2022-06-30 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]