from django.urls import path

from .views import (
    home,
    dashboard, 
    lista_habilidades_admin, crear_habilidad, editar_habilidad, eliminar_habilidad,
    lista_proyectos_admin, crear_proyecto_admin, editar_proyecto, eliminar_proyecto
)

urlpatterns = [
    # Rutas públicas
    path('', home, name="home"),
    
    # Rutas del panel de administración (usando panel/ en lugar de admin/)
    path('panel/dashboard/', dashboard, name="dashboard"),
    
    # Rutas de Habilidades
    path('panel/habilidades/', lista_habilidades_admin, name="lista_habilidades_admin"),
    path('panel/habilidades/crear/', crear_habilidad, name="crear_habilidad"),
    path('panel/habilidades/<int:pk>/editar/', editar_habilidad, name="editar_habilidad"),
    path('panel/habilidades/<int:pk>/eliminar/', eliminar_habilidad, name="eliminar_habilidad"),
    
    # Rutas de Proyectos
    path('panel/proyectos/', lista_proyectos_admin, name="lista_proyectos_admin"),
    path('panel/proyectos/crear/', crear_proyecto_admin, name="crear_proyecto_admin"),
    path('panel/proyectos/<int:pk>/editar/', editar_proyecto, name="editar_proyecto"),
    path('panel/proyectos/<int:pk>/eliminar/', eliminar_proyecto, name="eliminar_proyecto"),
]
