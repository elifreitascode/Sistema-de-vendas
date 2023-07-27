from django.db import models

class Vendas(models.Model):
    Cod = models.IntegerField()
    Situacao = models.CharField(max_length=65,default=True)
    Data = models.DateTimeField(auto_now_add=True)
    Nome_cliente = models.CharField(max_length=65,default=True)
    Sobrenome_cliente =  models.CharField(max_length=65, default=True)
    Preco_da_venda = models.DecimalField(decimal_places=2,max_digits=9)

    def __str__(self) -> str:
        return self.Nome_cliente
    
# Create your models here.
class Produtos(models.Model):
    Cod = models.IntegerField()
    SKU = models.CharField(max_length=65)
    Nome = models.CharField(max_length=65)
    Vendas = models.IntegerField()
    EstoqueTotal = models.IntegerField()
    CustoTotal = models.DecimalField(decimal_places=2, max_digits=9)
    RevendaTotal = models.DecimalField(decimal_places=2, max_digits=9)
    
    def __str__(self) -> str:
        return self.Nome