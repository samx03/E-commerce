# Generated by Django 3.1.7 on 2021-04-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
