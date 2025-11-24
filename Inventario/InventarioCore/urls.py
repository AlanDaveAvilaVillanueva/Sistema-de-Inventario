from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Inventario API')

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'categorias', views.CategoriaViewSet, basename='categoria')
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'movimientos', views.MovimientoInventarioViewSet, basename='movimientoinventario')

urlpatterns = [
    # API endpoints under /api/
    path('api/', include(router.urls)),

    # Home page
    path('', views.home, name='home'),

    # CRUD views (templates)
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/create/', views.UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/update/', views.UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<int:pk>/delete/', views.UsuarioDeleteView.as_view(), name='usuario-delete'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categorias/create/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),

    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('productos/create/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/update/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/delete/', views.ProductoDeleteView.as_view(), name='producto-delete'),

    path('movimientos/', views.MovimientoInventarioListView.as_view(), name='movimientoinventario-list'),
    path('movimientos/<int:pk>/', views.MovimientoInventarioDetailView.as_view(), name='movimientoinventario-detail'),
    path('movimientos/create/', views.MovimientoInventarioCreateView.as_view(), name='movimientoinventario-create'),
    path('movimientos/<int:pk>/update/', views.MovimientoInventarioUpdateView.as_view(), name='movimientoinventario-update'),
    path('movimientos/<int:pk>/delete/', views.MovimientoInventarioDeleteView.as_view(), name='movimientoinventario-delete'),
    path('export/productos/', views.export_products_csv, name='export-productos-csv'),

    # API schema (OpenAPI)
    path('api/schema/', schema_view, name='openapi-schema'),
]

