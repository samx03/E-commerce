from django.db import models


class top_Products(models.Model):
    Name_of_product = models.CharField(max_length=50)
    image_of_product = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.Name_of_product

    @staticmethod
    def get_all_top_Products():
        return top_Products.objects.all()
