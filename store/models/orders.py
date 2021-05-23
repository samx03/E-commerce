from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    firstName = models.CharField(max_length=50, default='', blank=True)
    lastName = models.CharField(max_length=50, default='', blank=True)
    streetName = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)
    pincode = models.CharField(max_length=6, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    completed = models.BooleanField(default=False)

    def total_price(self):
        total = self.quantity * self.price
        return total

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer=customer_id)\
            .order_by('-date')
