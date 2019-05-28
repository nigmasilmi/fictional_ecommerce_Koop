from django.db import models
from django.utils import timezone


class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='images/', default='koop.jpg')
    detalles = models.TextField(null=True, blank=False)
    precio = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True, blank=False)
    stock = models.IntegerField()
