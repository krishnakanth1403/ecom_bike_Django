from django.db import models
from account.models import User
# Create your models here.
class CompanyCategory(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_desc = models.TextField()
    unit_price = models.FloatField()
    company_category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(blank=True)
    stock = models.IntegerField()
    discount = models.FloatField(blank=True, null=True)
    reviews = models.TextField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return '{}' '-' '{}'.format(self.product_name, self.company_category)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.product_name

    def price(self):
        price = self.product.unit_price
        return price

    def total(self):
        total = self.quantity * self.product.unit_price
        return total

class Order(models.Model):
    statuses = [('A', 'Accepted')]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    total = models.IntegerField()
    status = models.CharField(max_length=10, choices=statuses, default='A')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name



