from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Producto


class ProductosListView(ListView):
    model = Producto
    context_object_name = 'productos_koop'
    template_name = 'lista_productos.html'


class ProductosDetailView(DetailView):
    queryset = Producto.objects.all()
    template_name = 'detalle_producto.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductosDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
