from django.db import models
from .category import Category
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    out_of_stock = models.BooleanField(default=False)
    description = RichTextUploadingField()
    caption = models.CharField(max_length=100, default='')
    video = models.FileField(upload_to='uploads/videos/', default='No video')
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();