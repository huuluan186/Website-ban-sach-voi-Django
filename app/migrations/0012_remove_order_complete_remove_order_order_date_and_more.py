# Generated by Django 5.1.2 on 2024-12-04 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]