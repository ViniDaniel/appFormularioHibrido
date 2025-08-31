from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Nome Completo"
    )
    email = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="E-Mail"
    )
    data_de_nascimento = models.DateField(
        null=False, blank=False, verbose_name="Data de Nascimento"
    )
    senha = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(5)],
        verbose_name="Senha",
    )

    def __str__(self):
        return self.nome
