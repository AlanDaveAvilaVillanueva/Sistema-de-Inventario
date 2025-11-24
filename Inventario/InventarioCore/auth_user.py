from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario


def create_usuario(username, email, raw_password):
    """Crea un Usuario con la contraseña hasheada y lo guarda en la BD.

    Uso:
        create_usuario('juan', 'juan@example.com', 'mi_password')
    """
    hashed = make_password(raw_password)
    user = Usuario.objects.create(username=username, email=email, password=hashed)
    return user


def set_password(usuario, raw_password):
    """Setea y persiste la contraseña hasheada para una instancia Usuario."""
    usuario.password = make_password(raw_password)
    usuario.save(update_fields=['password'])


def check_user_password(usuario, raw_password):
    """Devuelve True si `raw_password` coincide con la contraseña del usuario."""
    return check_password(raw_password, usuario.password)


# helpers para uso rápido en views/serializers

def authenticate_usuario(username, raw_password):
    """Autentica un usuario por username y contraseña. Devuelve el objeto Usuario o None
    """
    try:
        user = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        return None

    if check_password(raw_password, user.password):
        return user
    return None
