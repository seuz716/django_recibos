from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'  # Cambia el nombre del atributo



class ClienteMixin:
    model = Cliente
    form_class = ClienteForm
    context_object_name = 'cliente'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ClienteCreateView(SuccessMessageMixin, ClienteMixin, CreateView):
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('clientes:cliente_list')
    success_message = 'Cliente creado con éxito.'

class ClienteDetailView(ClienteMixin, DetailView):
    template_name = 'clientes/cliente_detail.html'

class ClienteUpdateView(SuccessMessageMixin, ClienteMixin, UpdateView):
    template_name = 'clientes/cliente_form.html'

    def get_success_url(self):
        return reverse_lazy('clientes:cliente_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Cliente actualizado con éxito.')
        return super().form_valid(form)

class ClienteDeleteView(ClienteMixin, DeleteView):
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:cliente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente eliminado con éxito.')
        return super().delete(request, *args, **kwargs)

