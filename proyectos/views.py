from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection

from .models import Proyecto, Habilidad
from .forms import ProyectoForm


# LISTA DE PROYECTOS
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "proyectos/lista.html", {"proyectos": proyectos})


# DETALLE DE PROYECTO
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, "proyectos/detalle.html", {"proyecto": proyecto})


# CREAR PROYECTO (opcional: @login_required)
def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProyectoForm()

    return render(request, "proyectos/crear.html", {"form": form})


# CONSULTA SQL (requisito explícito)
def consulta_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.titulo, h.nombre, h.experiencia
            FROM proyectos_proyecto p
            JOIN proyectos_proyecto_habilidades ph ON p.id = ph.proyecto_id
            JOIN proyectos_habilidad h ON h.id = ph.habilidad_id
            ORDER BY p.fecha_publicacion DESC;
        """)
        resultados = cursor.fetchall()

    return render(request, "proyectos/sql.html", {"resultados": resultados})

