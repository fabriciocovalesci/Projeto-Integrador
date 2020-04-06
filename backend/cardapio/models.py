from django.db import models
from backend.cafes.models import Cafes
from backend.doces.models import Doces
from backend.salgados.models import Salgados

class Cardapio(models.Model):
    nome = models.CharField(max_length=150)
    cafe = models.ForeignKey(Cafes, on_delete=models.CASCADE)
    doce = models.ForeignKey(Doces, on_delete=models.CASCADE)
    salgado = models.ForeignKey(Salgados, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

