from rest_framework.generics import ListAPIView

from productos.models import Producto
from .serializers import ProductoSerializer


class ListaProductosAPI(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
