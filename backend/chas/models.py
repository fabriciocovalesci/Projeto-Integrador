from django.db import models

class Chas(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ml = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    foto_chas = models.ImageField(
        upload_to='chas', null=True, blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cha"
        verbose_name_plural = "Chas"