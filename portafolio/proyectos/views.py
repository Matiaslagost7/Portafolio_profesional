from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views import View
from django.utils.decorators import method_decorator


from .models import Proyecto, Habilidad
from .forms import ProyectoForm, HabilidadForm
from login.mixins import solo_login_requerido

# HOME PAGE
def home(request):
    habilidades_tecnicas = Habilidad.objects.filter(tipo='tecnica')
    habilidades_blandas = Habilidad.objects.filter(tipo='blanda')
    proyectos = Proyecto.objects.all()
    return render(request, "home.html", {
        "habilidades_tecnicas": habilidades_tecnicas,
        "habilidades_blandas": habilidades_blandas,
        "proyectos": proyectos
    })




# ============= PANEL DE ADMINISTRACIÓN =============
# Nota: Los mixins LoginRequiredCustomMixin se usan en Class-Based Views (CBV)
# Ejemplo de uso:
# class DashboardView(LoginRequiredCustomMixin, View):
#     template_name = 'admin/dashboard.html'
#     def get(self, request):
#         ...
# En este proyecto usamos Function-Based Views con decoradores @solo_login_requerido

def es_admin(user):
    """Verifica si el usuario es superusuario"""
    return user.is_authenticated and user.is_superuser


@solo_login_requerido
def dashboard(request):
    """Panel principal de administración"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    context = {
        'total_proyectos': Proyecto.objects.count(),
        'total_habilidades': Habilidad.objects.count(),
    }
    return render(request, "panel_admin.html", context)


@solo_login_requerido
def lista_habilidades_admin(request):
    """Lista todas las habilidades en el panel, separadas por tipo"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    habilidades_tecnicas = Habilidad.objects.filter(tipo='tecnica')
    habilidades_blandas = Habilidad.objects.filter(tipo='blanda')
    return render(request, "habilidades/lista.html", {
        "habilidades_tecnicas": habilidades_tecnicas,
        "habilidades_blandas": habilidades_blandas
    })


@solo_login_requerido
def crear_habilidad(request):
    """Crear una nueva habilidad"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    if request.method == "POST":
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Habilidad creada exitosamente!")
            return redirect("lista_habilidades_admin")
    else:
        form = HabilidadForm()
    
    return render(request, "habilidades/form.html", {"form": form, "titulo": "Crear Habilidad"})


@solo_login_requerido
def editar_habilidad(request, pk):
    """Editar una habilidad existente"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    habilidad = get_object_or_404(Habilidad, pk=pk)
    
    if request.method == "POST":
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Habilidad actualizada exitosamente!")
            return redirect("lista_habilidades_admin")
    else:
        form = HabilidadForm(instance=habilidad)
    
    return render(request, "habilidades/form.html", {"form": form, "titulo": "Editar Habilidad", "habilidad": habilidad})


@solo_login_requerido
def eliminar_habilidad(request, pk):
    """Eliminar una habilidad"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    habilidad = get_object_or_404(Habilidad, pk=pk)
    
    if request.method == "POST":
        nombre = habilidad.nombre
        habilidad.delete()
        messages.success(request, f"¡Habilidad '{nombre}' eliminada exitosamente!")
        return redirect("lista_habilidades_admin")
    
    return render(request, "habilidades/confirmar_eliminar.html", {"objeto": habilidad})


@solo_login_requerido
def lista_proyectos_admin(request):
    """Lista todos los proyectos en el panel"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    proyectos = Proyecto.objects.all()
    return render(request, "proyectos/lista.html", {"proyectos": proyectos})


@solo_login_requerido
def crear_proyecto_admin(request):
    """Crear un nuevo proyecto"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Proyecto creado exitosamente!")
            return redirect("lista_proyectos_admin")
    else:
        form = ProyectoForm()
    
    return render(request, "proyectos/form.html", {"form": form, "titulo": "Crear Proyecto"})


@solo_login_requerido
def editar_proyecto(request, pk):
    """Editar un proyecto existente"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Proyecto actualizado exitosamente!")
            return redirect("lista_proyectos_admin")
    else:
        form = ProyectoForm(instance=proyecto)
    
    return render(request, "proyectos/form.html", {"form": form, "titulo": "Editar Proyecto", "proyecto": proyecto})


@solo_login_requerido
def eliminar_proyecto(request, pk):
    """Eliminar un proyecto"""
    if not es_admin(request.user):
        return HttpResponseForbidden("No tienes permiso para acceder al panel de administración")
    
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == "POST":
        titulo = proyecto.titulo
        proyecto.delete()
        messages.success(request, f"¡Proyecto '{titulo}' eliminado exitosamente!")
        return redirect("lista_proyectos_admin")
    
    return render(request, "proyectos/confirmar_eliminar.html", {"objeto": proyecto})

