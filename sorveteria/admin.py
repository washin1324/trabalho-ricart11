from django.contrib import admin
from .models import Cliente, Sabor, Pedido, Estoque

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Sabor)
admin.site.register(Pedido)
admin.site.register(Estoque)
