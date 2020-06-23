from django.contrib import admin
from .models import ProductCategory, Product, Client, Transaction


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('code', 'id')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Transaction, TransactionAdmin)
