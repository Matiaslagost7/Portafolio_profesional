from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Crea el primer usuario como superusuario si no existen usuarios. Usa variables de entorno en despliegues.'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.exists():
            self.stdout.write(self.style.WARNING('Ya existen usuarios. No se creó ningún superusuario.'))
            return

        username = os.environ.get('ADMIN_USER') or 'admin'
        email = os.environ.get('ADMIN_EMAIL') or 'admin@example.com'
        password = os.environ.get('ADMIN_PASSWORD') or 'admin123'

        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado correctamente.'))
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Error creando superusuario: {e}'))
