from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, default="")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """Setea (y persiste) la contraseña hasheada para este usuario."""
        self.password = make_password(raw_password)
        # Use update_fields to avoid touching other fields if caller saved before
        self.save(update_fields=['password'])

    def check_password(self, raw_password):
        """Verifica una contraseña en texto plano contra la almacenada."""
        return check_password(raw_password, self.password)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    cantidad = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre} ({self.categoria.nombre})'


class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.tipo.capitalize()} - {self.producto.nombre} - {self.cantidad}'




