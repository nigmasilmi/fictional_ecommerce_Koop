from .views import ListaProductosAPI

from django.urls import path, include

urlpatterns = [
    path('', ListaProductosAPI.as_view(), name='apiListaProductos')

]