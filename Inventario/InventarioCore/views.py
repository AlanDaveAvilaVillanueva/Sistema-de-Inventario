from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Usuario, Categoria, Producto, MovimientoInventario
from .serializers import (
    UsuarioSerializer,
    CategoriaSerializer,
    ProductoSerializer,
    MovimientoInventarioSerializer,
)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from django.urls import reverse_lazy
from django.shortcuts import render

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all()
    serializer_class = MovimientoInventarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------- Vistas basadas en clases para renderizar templates (CRUD) ---------



class UsuarioListView(LoginRequiredMixin, generic.ListView):
    model = Usuario
    template_name = 'usuario_list.html'


class UsuarioDetailView(LoginRequiredMixin, generic.DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'


class UsuarioCreateView(LoginRequiredMixin, generic.CreateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('usuario-list')


class UsuarioUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    template_name = 'usuario_form.html'
    fields = ['username', 'email']

    def get_success_url(self):
        return reverse_lazy('usuario-detail', kwargs={'pk': self.object.pk})


class UsuarioDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')


class CategoriaListView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'categoria_list.html'


class CategoriaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'


class CategoriaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria-list')


class CategoriaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['nombre', 'descripcion']

    def get_success_url(self):
        return reverse_lazy('categoria-detail', kwargs={'pk': self.object.pk})


class CategoriaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')


class ProductoListView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'producto_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        categoria = self.request.GET.get('categoria')
        if q:
            qs = qs.filter(nombre__icontains=q)
        if categoria:
            qs = qs.filter(categoria_id=categoria)
        return qs


class ProductoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Producto
    template_name = 'producto_detail.html'


class ProductoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'descripcion', 'categoria', 'cantidad', 'precio_unitario']
    success_url = reverse_lazy('producto-list')


class ProductoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'descripcion', 'categoria', 'cantidad', 'precio_unitario']

    def get_success_url(self):
        return reverse_lazy('producto-detail', kwargs={'pk': self.object.pk})


class ProductoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')


class MovimientoInventarioListView(LoginRequiredMixin, generic.ListView):
    model = MovimientoInventario
    template_name = 'movimiento_list.html'


class MovimientoInventarioDetailView(LoginRequiredMixin, generic.DetailView):
    model = MovimientoInventario
    template_name = 'movimiento_detail.html'


class MovimientoInventarioCreateView(LoginRequiredMixin, generic.CreateView):
    model = MovimientoInventario
    template_name = 'movimiento_form.html'
    fields = ['producto', 'tipo', 'cantidad', 'descripcion']
    success_url = reverse_lazy('movimientoinventario-list')


class MovimientoInventarioUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MovimientoInventario
    template_name = 'movimiento_form.html'
    fields = ['producto', 'tipo', 'cantidad', 'descripcion']

    def get_success_url(self):
        return reverse_lazy('movimientoinventario-detail', kwargs={'pk': self.object.pk})


class MovimientoInventarioDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MovimientoInventario
    template_name = 'movimiento_confirm_delete.html'
    success_url = reverse_lazy('movimientoinventario-list')


@login_required
def export_products_csv(request):
    """Exporta la lista de productos a CSV."""
    products = Producto.objects.select_related('categoria').all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Categoria', 'Cantidad', 'Precio'])
    for p in products:
        writer.writerow([p.id, p.nombre, p.categoria.nombre if p.categoria else '', p.cantidad, p.precio_unitario])
    return response


def home(request):
    """Renderiza la página principal (`base.html`)."""
    return render(request, 'base.html')

