# Sistema de Gestión de Inventario

Aplicación Django para el control de inventario de insumos y repuestos. Provee:

- CRUD para Usuarios, Categorías, Productos y Movimientos (entradas/salidas).
- API REST con Django REST Framework en `/api/`.
- Plantillas con Bootstrap para una interfaz rápida.
- Login/logout (vistas de Django) y protección básica de vistas.
- Exportación CSV para productos.

---

## Requisitos

- Python 3.10+
- MySQL o MariaDB
- pip
- (Windows) Visual C++ Build Tools si instalas `mysqlclient` desde código

Las dependencias están en `requirements.txt`.

## Instalación y configuración (Windows - PowerShell)

1. Clona el repositorio y entra en la carpeta del proyecto (la que contiene `manage.py`).

2. Crear y activar un entorno virtual:

```powershell
python -m venv venv
venv\Scripts\Activate
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

4. Crear archivo `.env` en la raíz del proyecto (misma carpeta que `README.md`) con las variables de conexión a la BD:

```env
DB_NAME=inventory_db
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_HOST=127.0.0.1
DB_PORT=3306
# SECRET_KEY=opcional_si_quieres_sobrescribir
```

> Nota: en `Inventario/Inventario/settings.py` se usan estas variables para configurar la conexión.

## mysqlclient en Windows

`mysqlclient` es la opción recomendada para Django+MySQL. En Windows puede requerir compilación:

- Opción A (recomendada): Instala "Build Tools for Visual Studio" (compilación C++) y luego:

```powershell
pip install mysqlclient
```

- Opción B: descargar una rueda (wheel) precompilada compatible con tu versión de Python y luego:

```powershell
pip install C:\ruta\a\mysqlclient‑<versión>‑cpXY‑cpXYm‑win_amd64.whl
```

- Opción C (si no quieres dependencias nativas): usar `mysql-connector-python` como alternativa (puede requerir ajustes en algunos casos).

Si tienes problemas al instalar `mysqlclient`, copia el error aquí y te ayudo.

## Migraciones y primer arranque

Ejecuta las migraciones, crea un superusuario y levanta el servidor:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en el navegador.

## Rutas principales

- Página principal (templates): `/`.
- Usuarios (CRUD): `/usuarios/`.
- Categorías (CRUD): `/categorias/`.
- Productos (CRUD): `/productos/`.
- Movimientos (CRUD): `/movimientos/`.
- Exportar productos CSV (login requerido): `/export/productos/`.
- API REST: `/api/` (ej.: `/api/productos/`).
- OpenAPI schema: `/api/schema/`.
- Login/Logout: `/accounts/login/`, `/accounts/logout/`.

## Uso rápido

- Buscar productos: `GET /productos/?q=termino`.
- Paginación disponible en la lista de productos.

## Seguridad y despliegue

- No publiques `.env` ni credenciales. Añade `.env` a `.gitignore` si procede.
- Para producción: `DEBUG = False`, configura `ALLOWED_HOSTS`, usa un servidor WSGI/ASGI y HTTPS.

## Mejoras sugeridas

- Migrar a `AbstractUser` si necesitas expandir el modelo de usuario.
- Añadir tests automatizados.
- Añadir Dockerfile/docker-compose para despliegue.
- Documentación de la API más completa (Swagger/Redoc).

---

Si quieres, puedo: añadir Bootstrap completo a todas las plantillas, crear un `docker-compose.yml`, o migrar a `AbstractUser`. Dime qué prefieres y lo implemento.
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




