from django.db import models
from django.contrib.auth import get_user_model

from desafio_ibm.users.models import City

User = get_user_model()


class CommonControlField(models.Model):
    """
    Classe com campos de controle
    """

    created = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)

    updated = models.DateTimeField(
        verbose_name="Data da última atualização", auto_now=True
    )

    creator = models.ForeignKey(
        User,
        verbose_name="Criador",
        related_name="%(class)s_creator",
        editable=False,
        on_delete=models.CASCADE,
    )

    updated_by = models.ForeignKey(
        User,
        verbose_name="Modificador",
        related_name="%(class)s_last_mod_user",
        editable=False,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Pet(CommonControlField):
    """
    Essa classe representa um pet.

    Campos:
        Nome do Cidade
    """

    name = models.CharField("Nome", blank=True, max_length=255)
    race = models.CharField("Raça", blank=True, max_length=255)
    age = models.CharField("Idade", blank=True, max_length=255)
    weight = models.CharField("Peso", blank=True, max_length=255)

    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, verbose_name="Cidade", null=True, blank=True
    )

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pet"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
