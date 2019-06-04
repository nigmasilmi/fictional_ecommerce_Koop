"""KoopSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, about_view, contact_view, register_view, login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('contact/', contact_view, name="contacto"),
                  path('login/', login_view, name="login"),
                  path('register/', register_view, name="registro"),
                  path('about/', about_view, name="acerca_de"),
                  path('catalogo/', include('productos.urls')),
                  path('api/catalogo/', include('productos.api.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)