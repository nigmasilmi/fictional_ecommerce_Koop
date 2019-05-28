from django.urls import path, include
from .views import productos_list_view

urlpatterns = [
    path('', productos_list_view, name="lista_productos"),

]
