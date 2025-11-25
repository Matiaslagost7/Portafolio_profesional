#!/bin/bash
# Script de arranque para Render.
# Todos los comandos se ejecutan desde la raíz del repositorio.
set -euo pipefail

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python portafolio/manage.py migrate --noinput || {
    echo "❌ Error en migraciones"
    exit 1
}

# Recolectar archivos estáticos (limpiando el destino primero)
echo "Recolectando archivos estáticos..."
python portafolio/manage.py collectstatic --noinput --clear || {
    echo "❌ Error al recolectar estáticos"
    exit 1
}

# Crear superuser si no existe
echo "Verificando superuser..."
python portafolio/manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('✅ Superuser creado')
else:
    print('✅ Superuser ya existe')
END

# Arrancar Gunicorn
echo "✅ Iniciando Gunicorn..."
exec gunicorn portafolio.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --access-logfile - \
    --error-logfile - \
    --log-level info \
    --capture-output
