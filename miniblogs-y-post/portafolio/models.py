from django.db import models

# Creacion de formularios para base de datos

class Projecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="portafolio/imagenes/")
    # Url opcional con blank=True
    url = models.URLField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Muestra este nombre en el panel de admin
    def __str__(self):
        return self.titulo