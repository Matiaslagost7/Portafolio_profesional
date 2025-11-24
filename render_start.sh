#!/bin/bash
# Script de arranque para Render: usa manage.py dentro de la carpeta del proyecto.
set -euo pipefail

python portafolio/manage.py migrate --noinput
python portafolio/manage.py collectstatic --noinput
python portafolio/manage.py createsuperifnone < /dev/null || true

# Arrancar Gunicorn apuntando al módulo WSGI correcto
exec gunicorn portafolio.wsgi:application
