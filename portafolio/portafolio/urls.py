from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from portafolio.health_checks import health_check, ready_check

urlpatterns = [
    # Health checks para Render
    path('health/', health_check, name='health_check'),
    path('ready/', ready_check, name='ready_check'),
    
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),  # URLs de autenticación
    path('', include('proyectos.urls')),  # Proyectos y home
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
