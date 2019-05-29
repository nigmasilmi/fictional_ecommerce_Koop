from rest_framework.serializers import ModelSerializer
from ..models import Producto


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'categoria', 'detalles', 'precio', 'fecha_ingreso', 'stock']
