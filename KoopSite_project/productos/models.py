from django.db import models


class Producto(models.Model):
    CATEGORIA_CHOICES = [

        ('electronics', 'Electrónicos'),
        ('sports', 'Deportes'),
        ('other', 'Misceláneos')
    ]
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='other')
    imagen = models.ImageField(upload_to='images/', default='koop.jpg')
    detalles = models.TextField(null=True, blank=False)
    precio = models.FloatField(default=10.990)
    fecha_ingreso = models.DateField(auto_now_add=True, blank=False)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
