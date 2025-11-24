from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import MovimientoInventario, Producto

# Señales para mantener sincronizado el stock del producto cuando se crean/actualizan/eliminan movimientos
def _effect_of(movimiento: MovimientoInventario) -> int:
    """Devuelve el efecto numérico sobre el stock: +cantidad para 'entrada', -cantidad para 'salida'."""
    return movimiento.cantidad if movimiento.tipo == 'entrada' else -movimiento.cantidad


@receiver(post_save, sender=MovimientoInventario)
def _movimiento_post_save(sender, instance: MovimientoInventario, created, **kwargs):
    if not created:
        return
    effect = _effect_of(instance)
    producto = instance.producto
    if producto.cantidad + effect < 0:
        raise ValidationError('Stock insuficiente para aplicar este movimiento.')
    producto.cantidad = producto.cantidad + effect
    producto.save()


@receiver(pre_save, sender=MovimientoInventario)
def _movimiento_pre_save(sender, instance: MovimientoInventario, **kwargs):
    # Si existe, comparar con el anterior para ajustar stock en consecuencia
    if not instance.pk:
        return
    try:
        old = MovimientoInventario.objects.get(pk=instance.pk)
    except MovimientoInventario.DoesNotExist:
        return

    old_effect = _effect_of(old)
    new_effect = _effect_of(instance)

    # Mismo producto -> aplicar delta
    if old.producto_id == instance.producto_id:
        delta = new_effect - old_effect
        producto = instance.producto
        if producto.cantidad + delta < 0:
            raise ValidationError('Actualización inválida: deja stock negativo.')
        producto.cantidad = producto.cantidad + delta
        producto.save()
    else:
        # Producto distinto: revertir efecto en producto antiguo y aplicar en el nuevo
        old_product = old.producto
        new_product = instance.producto

        # Revertir efecto antiguo
        if old_product.cantidad - old_effect < 0:
            raise ValidationError('No se puede revertir movimiento en el producto anterior (stock insuficiente).')
        old_product.cantidad = old_product.cantidad - old_effect
        old_product.save()

        # Aplicar efecto nuevo
        if new_product.cantidad + new_effect < 0:
            raise ValidationError('No se puede aplicar movimiento en el nuevo producto (stock insuficiente).')
        new_product.cantidad = new_product.cantidad + new_effect
        new_product.save()


@receiver(post_delete, sender=MovimientoInventario)
def _movimiento_post_delete(sender, instance: MovimientoInventario, **kwargs):
    # Al eliminar un movimiento, se revierte su efecto
    effect = _effect_of(instance)
    producto = instance.producto
    reverse = -effect
    if producto.cantidad + reverse < 0:
        raise ValidationError('No se puede eliminar este movimiento porque dejaría stock negativo.')
    producto.cantidad = producto.cantidad + reverse
    producto.save()