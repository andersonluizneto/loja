# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import string

class Municipio(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    iduf = models.ForeignKey('Uf', models.DO_NOTHING, db_column='IdUF')  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'Municipio'
        ordering = ['nome']


class Uf(models.Model):
    id = models.SmallIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=2)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'UF'
        ordering = ['sigla']


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, auto_now=False)
    email = models.CharField(max_length=100, null=True)
    endereco = models.CharField(verbose_name='endereço', max_length=100, null=True)
    cep = models.CharField(max_length=9, null=True)
    complemento = models.CharField(max_length=20, null=True)
    bairro = models.CharField(max_length=60, null=True)
    cidade = models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name='cidade', null=True)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE, verbose_name='estado', null=True)
    telefone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'Cliente'
        ordering = ['nome']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'



class Categoria(models.Model):
    categoria = models.CharField(max_length=80)
    categoria_pai = models.ForeignKey('self', null=True, related_name='Subcategoria')

    def __str__(self):
        return self.categoria

    class Meta:
        managed = True
        db_table = 'Categoria'
        ordering = ['categoria']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Produto(models.Model):
    nome = models.CharField("Nome", max_length=80)
    descricao = models.TextField("Descrição")
    imagem = models.FileField()
    preço = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        ordering = ['nome']
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        db_table = "Produto"


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, primary_key=True)
    quantidade = models.IntegerField()
    minimo = models.IntegerField(verbose_name='estoque mínimo', default=0)

    def __self__(self):
        estoque_str = 'Produto: {0} - Qtd: {1}'
        return estoque_str.format(self.produto.nome, self.quantidade)

    class Meta:
        managed = True
        ordering = ['quantidade']
        verbose_name = "estoque"
        db_table = "Estoque"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    status = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(verbose_name='data pedido', auto_now_add=True, auto_now=False)
    data_envio = models.DateTimeField(verbose_name='data envio', blank=True)
    data_entrega = models.DateTimeField(verbose_name='data entrega', blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    itens = models.ManyToManyField(Produto, through="ItensPedido")

    class Meta:
        managed = True
        ordering = ['data_pedido']
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        db_table = "Pedido"


class ItensPedido(models.Model):
    produto = models.ForeignKey(Produto)
    pedido = models.ForeignKey(Pedido)
    quantidade = models.IntegerField()
    preco = models.DecimalField(verbose_name='preço', max_digits=8, decimal_places=2)

    class Meta:
        managed = True
        verbose_name = "itens_pedido"
        verbose_name_plural = "itens_pedidos"
        db_table = "Intens_Pedidos"
