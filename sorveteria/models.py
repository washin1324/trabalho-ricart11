from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Sabor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    sabores = models.ManyToManyField(Sabor)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_pedido}"
    
class Estoque(models.Model):
    nome = models.CharField(max_length=255)
    sabor = models.OneToOneField('Sabor', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sabor.nome} - {self.quantidade} unidades"
