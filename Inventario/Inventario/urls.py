"""
URL configuration for Inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from ..InventarioCore import views

def home(request):
    return HttpResponse("Template de ejemplo para la página de inicio.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('InventarioCore.urls')),
    path('', home),  # <-- esto agrega una vista para la raíz

    path('usuarios/', views.UsuarioListView.as_view(), name='usuario-list'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('movimientos/', views.MovimientoInventarioListView.as_view(), name='movimientoinventario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('movimientos/<int:pk>/', views.MovimientoInventarioDetailView.as_view(), name='movimientoinventario-detail'),
    path('usuarios/create/', views.UsuarioCreateView.as_view(), name='usuario-create'),
    path('categorias/create/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('productos/create/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('movimientos/create/', views.MovimientoInventarioCreateView.as_view(), name='movimientoinventario-create'),
    path('usuarios/<int:pk>/update/', views.UsuarioUpdateView.as_view(), name='usuario-update'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('productos/<int:pk>/update/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('movimientos/<int:pk>/update/', views.MovimientoInventarioUpdateView.as_view(), name='movimientoinventario-update'),
    path('usuarios/<int:pk>/delete/', views.UsuarioDeleteView.as_view(), name='usuario-delete'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('productos/<int:pk>/delete/', views.ProductoDeleteView.as_view(), name='producto-delete'),
    path('movimientos/<int:pk>/delete/', views.MovimientoInventarioDeleteView.as_view(), name='movimientoinventario-delete'),
]

    
