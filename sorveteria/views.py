from typing import Any
from django.shortcuts import render, redirect
from .models import Cliente, Sabor, Pedido, Estoque
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class home_page(View):
  def get(self, request):
    return render(request, 'home-page.html')

class cliente_list(ListView):
  model = Cliente

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Cliente.objects.all(), 'Entity': 'Clientes'})

class sabor_list(ListView):
  model = Sabor

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Sabor.objects.all(), 'Entity': 'Sabores'})

class pedido_list(ListView):
  model = Pedido

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Pedido.objects.all(), 'Entity': 'Pedidos'})

class estoque_list(ListView):
  model = Estoque

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Estoque.objects.all(), 'Entity': 'Estoque'})
  
class cliente_add(CreateView):
  model = Cliente
  fields = ['nome', 'email']
  template_name = 'form.html'
  success_url = '/sorveteria/clientes'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Clientes'
    return context
  
class sabor_add(CreateView):
  model = Sabor
  fields = ['nome', 'descricao']
  template_name = 'form.html'
  success_url = '/sorveteria/sabores'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Sabores'
    return context

class pedido_add(CreateView):
  model = Pedido
  fields = ['nome', 'cliente', 'sabores']
  template_name = 'form.html'
  success_url = '/sorveteria/pedidos'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Pedidos'
    return context
  
class estoque_add(CreateView):
  model = Estoque
  fields = ['nome', 'sabor', 'quantidade']
  template_name = 'form.html'
  success_url = '/sorveteria/estoque'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Estoque'
    return context

class cliente_detail(DetailView):
  model = Cliente
  template_name = 'instance-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    fields = context['object']._meta.get_fields()
    field_values = {field.name: getattr(context['object'], field.name) for field in fields if hasattr(context['object'], field.name)}
    context['object'] = field_values
    context['Entity'] = 'clientes'
    return context

class sabor_detail(DetailView):
  model = Sabor
  template_name = 'instance-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    fields = context['object']._meta.get_fields()
    field_values = {field.name: getattr(context['object'], field.name) for field in fields if hasattr(context['object'], field.name)}
    context['object'] = field_values
    context['Entity'] = 'sabores'
    return context

class pedido_detail(DetailView):
  model = Pedido
  template_name = 'instance-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    fields = context['object']._meta.get_fields()
    field_values = {field.name: getattr(context['object'], field.name) for field in fields if hasattr(context['object'], field.name)}
    context['object'] = field_values
    context['Entity'] = 'pedidos'
    return context

class estoque_detail(DetailView):
  model = Estoque
  template_name = 'instance-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    fields = context['object']._meta.get_fields()
    field_values = {field.name: getattr(context['object'], field.name) for field in fields if hasattr(context['object'], field.name)}
    context['object'] = field_values
    context['Entity'] = 'estoque'
    return context

class cliente_update(UpdateView):
  model = Cliente
  fields = ['nome', 'email']
  template_name = 'form.html'
  success_url = '/sorveteria/clientes'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Clientes'
    return context

class sabor_update(UpdateView):
  model = Sabor
  fields = ['nome', 'descricao']
  template_name = 'form.html'
  success_url = '/sorveteria/sabores'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Sabores'
    return context

class pedido_update(UpdateView):
  model = Pedido
  fields = ['nome', 'cliente', 'sabores']
  template_name = 'form.html'
  success_url = '/sorveteria/pedidos'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Pedidos'
    return context

class estoque_update(UpdateView):
  model = Estoque
  fields = ['nome', 'sabor', 'quantidade']
  template_name = 'form.html'
  success_url = '/sorveteria/estoque'

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Estoque'
    return context

class cliente_delete(DeleteView):
  model = Cliente
  success_url = '/sorveteria/clientes'
  template_name = 'delete-object.html'

class sabor_delete(DeleteView):
  model = Sabor
  success_url = '/sorveteria/sabores'
  template_name = 'delete-object.html'

class pedido_delete(DeleteView):
  model = Pedido
  success_url = '/sorveteria/pedidos'
  template_name = 'delete-object.html'

class estoque_delete(DeleteView):
  model = Estoque
  success_url = '/sorveteria/estoque'
  template_name = 'delete-object.html'
