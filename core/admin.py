from django.contrib import admin

from .models import Product, Cliente


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cliente, ClienteAdmin)  