from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import PrimaryKeyConstraint, null


# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    product = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    sub_category = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    sale_price = models.IntegerField(null=True)
    market_price = models.IntegerField(null=True)
    product_type = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    description = models.CharField(max_length=1000, null=True)
    total_quantity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.auto_increment_id} - {self.product} - {self.order_quantity}'
