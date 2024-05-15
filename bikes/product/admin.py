from django.contrib import admin
from product.models import CompanyCategory, Product, Cart, Order
# Register your models here.

admin.site.register(CompanyCategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)