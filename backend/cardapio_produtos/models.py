from django.db import models
from backend.cafes.models import Cafes
from backend.doces.models import Doces
from backend.salgados.models import Salgados
from backend.chas.models import Chas
from backend.bebidas.models import Bebidas

class CardapioProduto(models.Model):
    nome = models.CharField(max_length=150)
    cafe = models.ManyToManyField(Cafes)
    doce = models.ManyToManyField(Doces)
    salgado = models.ManyToManyField(Salgados)
    chas = models.ManyToManyField(Chas)
    bebidas = models.ManyToManyField(Bebidas)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "CardapioProduto"
        verbose_name_plural = "CardapioProdutos"

