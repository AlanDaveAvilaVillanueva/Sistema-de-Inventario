# Sistema de Gestión de Inventario

## Como crear el entorno virtual
Para iniciar el entorno virtual y descargar todas las dependencias, debes seguir los siguientes pasos:
1. Abre una nueva terminal en ***Visual Studio Code***
2. Ingresa los siguientes codigos en orden:

**Crea el entonrno virtual**
```bash
python -m venv venv
```

**Activa el entorno virtual**
```bash
venv\Scripts\activate
```

**Descarga las dependencias**
```bash
pip install -r requirements.txt
```

Ya con eso deberías tener el entorno virtual listo para poder trabajar en este repositorio

---

## Como conectar MySQL

### creacion de archivo .env
Este archivo es indispensable para poder iniciar el servidor MySQL, ya que en ***Inventario > Settings*** se encuentra configurado para que encuentre el archivo **.env** y que recoja los datos ingresado en **.env**

1. Se crea fuera de las carpetas, al mismo nivel que **README.md**
2. El archivo se debe llamar unicamente **.env**
3. Dentro del archivo debe ir lo siguiente:
```bash
SECRET_KEY=
NAME= root
USER= root
DATABASE= invDB
PASSWORD_DB=
PORT= 3306
HOST= localhost
```
4. **invDB** es el nombre de la Base de Datos, tu **SCHEMA** en MySQL debe tener el mismo nombre (si no, no conectará con la base de datos)
5. La contraseña root debe ser la misma que hayas definido en la instalación de MySQL
6. **PORT** también debe ser el mismo que hayas definido en la instalación
7. **SECRET_KEY** debe ser creado en la terminal con el siguiente comando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
8. Debes copiar la SECRET_KEY que te haya dado la terminal y pegarlo en el archivo .env en **SECRET_KEY**


## Como iniciar Proyecto

## Recomendaciones




