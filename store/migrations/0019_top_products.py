# Generated by Django 3.1.7 on 2021-04-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_product_out_of_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='top_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
