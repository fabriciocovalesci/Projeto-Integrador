from django.db import models
from backend.cafes.models import Cafes
from backend.doces.models import Doces
from backend.salgados.models import Salgados

class Cardapio(models.Model):
    nome = models.CharField(max_length=150)
    cafe = models.ManyToManyField(Cafes)
    doce = models.ManyToManyField(Doces)
    salgado = models.ManyToManyField(Salgados)

    def __str__(self):
        return self.nome

