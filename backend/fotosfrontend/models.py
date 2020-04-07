from django.db import models

class FotosFrontend(models.Model):
    foto_frontend = models.ImageField(upload_to='fotosfrontend', null=True, blank=True)
