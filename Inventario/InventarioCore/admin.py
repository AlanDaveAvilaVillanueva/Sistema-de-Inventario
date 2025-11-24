from django.contrib import admin
from .models import Usuario, Categoria, Producto, MovimientoInventario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'fecha_registro')
    search_fields = ('username', 'email')
    list_filter = ('fecha_registro',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ()


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'cantidad', 'precio_unitario')
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria',)
    

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'tipo', 'cantidad', 'fecha')
    search_fields = ('producto__nombre', 'tipo')
    list_filter = ('tipo', 'fecha')
