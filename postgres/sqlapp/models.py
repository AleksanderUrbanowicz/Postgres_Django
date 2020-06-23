from django.db import models
from datetime import datetime


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    code = models.CharField(max_length=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    transaction_date = models.DateField(default=datetime.today)

    def __str__(self):
        return f' {self.code} - {self.amount} {self.product.name} for: {self.client.name}'
