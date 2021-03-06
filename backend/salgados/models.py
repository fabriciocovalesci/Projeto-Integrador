from django.db import models

class Salgados(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    unidades = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    foto_salgados = models.ImageField(upload_to='salgados', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Salgado"
        verbose_name_plural = "Salgados"