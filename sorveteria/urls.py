from django.urls import path
from . import views

urlpatterns = [
  path('clientes/', views.cliente_list.as_view(), name='clientes'),
  path('clientes/detalhes/<int:pk>', views.cliente_detail.as_view(), name='detalhes_cliente'),
  path('clientes/adicionar', views.cliente_add.as_view(), name='adicionar_cliente'),
  path('clientes/editar/<int:pk>', views.cliente_update.as_view(), name='editar_cliente'),
  path('clientes/deletar/<int:pk>', views.cliente_delete.as_view(), name='deletar_cliente'),
  path('sabores/', views.sabor_list.as_view(), name='sabores'),
  path('sabores/detalhes/<int:pk>', views.sabor_detail.as_view(), name='detalhes_sabor'),
  path('sabores/adicionar', views.sabor_add.as_view(), name='adicionar_sabor'),
  path('sabores/editar/<int:pk>', views.sabor_update.as_view(), name='editar_sabor'),
  path('sabores/deletar/<int:pk>', views.sabor_delete.as_view(), name='deletar_sabor'),
  path('pedidos/', views.pedido_list.as_view(), name='pedidos'),
  path('pedidos/detalhes/<int:pk>', views.pedido_detail.as_view(), name='detalhes_pedido'),
  path('pedidos/adicionar', views.pedido_add.as_view(), name='adicionar_pedido'),
  path('pedidos/editar/<int:pk>', views.pedido_update.as_view(), name='editar_pedido'),
  path('pedidos/deletar/<int:pk>', views.pedido_delete.as_view(), name='deletar_pedido'),
  path('estoque/', views.estoque_list.as_view(), name='estoque'),
  path('estoque/detalhes/<int:pk>', views.estoque_detail.as_view(), name='detalhes_estoque'),
  path('estoque/adicionar', views.estoque_add.as_view(), name='adicionar_estoque'),
  path('estoque/editar/<int:pk>', views.estoque_update.as_view(), name='editar_estoque'),
  path('estoque/deletar/<int:pk>', views.estoque_delete.as_view(), name='deletar_estoque'),
  path('', views.home_page.as_view(), name='home_page'),
]