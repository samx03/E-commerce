from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.topSelling import top_Products
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['username', 'email']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity' , 'price', 'total_price', 'streetName', 'city', 'state', 'pincode', 'phone', 'date', 'completed']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(top_Products)
admin.site.register(Order, AdminOrder)
