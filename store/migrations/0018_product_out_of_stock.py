# Generated by Django 3.1.7 on 2021-04-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_order_stock_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]
