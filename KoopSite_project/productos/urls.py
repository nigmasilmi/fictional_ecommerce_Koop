from django.urls import path, include
from .views import ProductosListView, ProductosDetailView


urlpatterns = [
    path('', ProductosListView.as_view(), name='lista_productos'),
    path('<pk>/', ProductosDetailView.as_view(), name='detalle_producto'),

]
