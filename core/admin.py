from django.contrib import admin
from .models import Cliente, Produto, Categoria, Estoque, Pedido, ItensPedido


@admin.register(Cliente, Produto, Categoria, Estoque, Pedido, ItensPedido)
class AuthorAdmin(admin.ModelAdmin):
    pass

