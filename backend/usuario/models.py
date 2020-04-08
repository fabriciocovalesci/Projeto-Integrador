from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, blank=True, null=True)
    telefone =  models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    data_nascimento = models.DateTimeField()
    endereco = models.CharField(max_length=150)
    foto_usuario = models.ImageField(
        upload_to='usuario', null=True, blank=True)


    def __str__(self):
        return self.nome.username

"""
Nome.
telefone.
email.
endereço.
sexo.
data de nascimento.
foto para perfil.
senha para acesso.
"""