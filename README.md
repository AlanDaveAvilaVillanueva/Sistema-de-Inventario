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


