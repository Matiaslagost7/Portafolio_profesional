from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crea el primer usuario como superusuario si no existen usuarios.'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.exists():
            username = input('Nombre de usuario para el superusuario: ')
            email = input('Email: ')
            password = input('Contraseña: ')
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superusuario creado correctamente.'))
        else:
            self.stdout.write(self.style.WARNING('Ya existen usuarios. No se creó ningún superusuario.'))
