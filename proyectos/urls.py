from django.urls import path
from .views import lista_proyectos, detalle_proyecto, crear_proyecto, consulta_sql

urlpatterns = [
    path('', lista_proyectos, name="lista_proyectos"),
    path('<int:pk>/', detalle_proyecto, name="detalle_proyecto"),
    path('crear/', crear_proyecto, name="crear_proyecto"),
    path('sql/', consulta_sql, name="consulta_sql"),
]
