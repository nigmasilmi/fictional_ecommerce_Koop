from django.db import models
from django.utils import timezone


class Producto(models.Model):

    CATEGORIA_CHOICES = [

        ('electronics', 'Electrónicos'),
        ('sports', 'Deportes'),
        ('other', 'Misceláneos')
    ]
    codigo = models.IntegerField()
    print(1)
    nombre = models.CharField(max_length=100)
    print(2)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='other')
    print(3)
    imagen = models.ImageField(upload_to='images/', default='koop.jpg')
    detalles = models.TextField(null=True, blank=False)
    precio = models.FloatField(default=10.990)
    print(4)
    fecha_ingreso = models.DateField(auto_now_add=True, blank=False)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
