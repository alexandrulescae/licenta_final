from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    verbose_name_plural = 'Categories'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address', 'status']


admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)



