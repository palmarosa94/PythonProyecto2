
from django.shortcuts import render, redirect
from .forms import PagoForm
from .models import Pagos
from coder.models import Abogados
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class PagosListView(ListView):
    model= Pagos
    template_name = 'pagos/lista_pagos.html'
    context_object_name = 'pagos'
    
    def get_queryset(self):
        return Pagos.objects.filter()    

class PagosCreateView(CreateView):
    model = Pagos
    form_class = PagoForm
    template_name = 'pagos/crear_pago.html'
    success_url = reverse_lazy('lista_pagos')
    
    def form_valid(self, form):
        return super().form_valid(form)


class PagosUpdateView(UpdateView):
    model = Pagos
    form_class = PagoForm
    template_name = 'pagos/editar_pago.html'
    success_url = reverse_lazy('lista_pagos')

    
class PagosDeleteView(DeleteView):
    model = Pagos
    template_name = 'pagos/borrar_pago.html'
    success_url = reverse_lazy('lista_pagos')


class PagosDetailView(DetailView):
    model = Pagos
    template_name = 'pagos/detalle_pago.html'
    context_object_name = 'pago'

