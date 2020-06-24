from django.db import models
from datetime import datetime

GENDER_CHOICES =[
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unspecified'),
]


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    def __str__(self):
        where_from = f'{self.city}, ' if self.city is not None else ''
        where_from += f' {self.country}'
        return f'{self.name} from {where_from}'

    class Meta:
        db_table = "clients"


class Transaction(models.Model):
    code = models.CharField(max_length=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    transaction_date = models.DateField(default=datetime.today)

    def __str__(self):
        return f' {self.code} - {self.amount} {self.product.name} for: {self.client.name}'

    class Meta:
        db_table = "transactions"
