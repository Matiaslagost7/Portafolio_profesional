from django.db import models

class Habilidad(models.Model):
    TIPO_CHOICES = [
        ("tecnica", "Técnica"),
        ("blanda", "Blanda"),
    ]
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default="tecnica")
    icono_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL del icono de la habilidad (ej: Font Awesome, Bootstrap Icons)"
    )
    
    class Meta:
        ordering = ['nombre'] 
    
    def __str__(self):
        return str(self.nombre)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    demo_url = models.URLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    
    habilidades = models.ManyToManyField(Habilidad, related_name='proyectos')
    class Meta:
        ordering = ['fecha_publicacion']
    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"[Proyecto.save] Guardando proyecto: {self.titulo}")
        if self.imagen:
            logger.info(f"[Proyecto.save] Imagen a guardar: {self.imagen.name}")
        try:
            super().save(*args, **kwargs)
            logger.info(f"[Proyecto.save] Proyecto guardado correctamente: {self.titulo}")
        except Exception as e:
            logger.error(f"[Proyecto.save] Error al guardar el proyecto o la imagen: {e}")
            raise