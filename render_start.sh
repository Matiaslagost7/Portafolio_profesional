#!/bin/bash
# Script para ejecutar migraciones y crear superusuario si no existen usuarios
python manage.py migrate --noinput
python manage.py createsuperifnone < /dev/null
exec gunicorn portafolio.wsgi:application
