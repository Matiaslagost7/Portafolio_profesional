"""
WSGI config for portafolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')

# Configurar logging para errores de aplicación
logger = logging.getLogger(__name__)

try:
    application = get_wsgi_application()
except Exception as e:
    logger.exception('Error al inicializar la aplicación WSGI')
    raise
