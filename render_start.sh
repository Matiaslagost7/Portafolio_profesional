#!/bin/bash
# Script de arranque para Render: usa manage.py dentro de la carpeta del proyecto.
set -euo pipefail

cd portafolio
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperifnone < /dev/null || true

# Arrancar Gunicorn con logging detallado
exec gunicorn portafolio.wsgi:application --bind 0.0.0.0:8000 --access-logfile - --error-logfile - --log-level debug
