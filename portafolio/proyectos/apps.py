from django.apps import AppConfig



class ProyectosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proyectos'

    # def ready(self):
    #     Diagnóstico eliminado para evitar errores de inicialización temprana
