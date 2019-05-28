from django.shortcuts import render
from .models import Producto


def productos_list_view(request):
    qs = Producto.objects.all()
    print(qs)
    for item in qs:
        print(item.nombre)
        print(item.imagen.url)
    title = 'Lista de productos disponibles'
    template_name = 'lista_productos.html'
    return render(request, template_name, {'query_set': qs, 'title': title})
