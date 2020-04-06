from django.db import models

class Doces(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    unidades = models.IntegerField()
    preco = models.DecimalField(max_digits=5,  decimal_places=2)
    foto_doces = models.ImageField(
        upload_to='doces', null=True, blank=True)

    def __str__(self):
        return self.nome


