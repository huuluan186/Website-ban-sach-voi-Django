# Generated by Django 5.1.4 on 2024-12-14 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]