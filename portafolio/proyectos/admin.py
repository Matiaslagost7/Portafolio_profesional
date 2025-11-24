from django.contrib import admin
from .models import Habilidad, Proyecto

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo")
    list_filter = ("tipo",)
    search_fields = ("nombre",)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    pass