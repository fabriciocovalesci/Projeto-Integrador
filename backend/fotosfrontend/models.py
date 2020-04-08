from django.db import models

class FotosFrontend(models.Model):
    descricao = models.CharField(max_length=150 , blank=True, null=True)
    foto_frontend = models.ImageField(upload_to='fotosfrontend', null=True, blank=True)

