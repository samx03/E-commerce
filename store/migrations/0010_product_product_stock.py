# Generated by Django 3.1.7 on 2021-04-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210423_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(default=0),
        ),
    ]