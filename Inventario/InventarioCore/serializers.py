from models import *
from rest_framework import serializers

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        field = '__all__'

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        field = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        field = '__all__'
    
class MovimientoInventarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventario
        field = '__all__'