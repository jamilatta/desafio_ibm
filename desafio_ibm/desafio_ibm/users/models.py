from django.db import models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class City(models.Model):
    """
    Representa uma lista de cidade

    Campos:
        Nome do Cidade
    """

    name = models.CharField("Nome da Cidade", blank=True, max_length=255)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class State(models.Model):
    """
    Representa uma lista de estados

    Campos:
        Nome do Estado
        Acrônimo
    """

    name = models.CharField("Nome do Estado", blank=True, max_length=255)
    acronym = models.CharField("Acrônimo do Estado", blank=True, max_length=255)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class User(AbstractUser):
    """Default user for desafio_ibm."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField("Nome", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    street = models.CharField("Rua", blank=True, max_length=255)
    street_number = models.CharField("Número", blank=True, max_length=10)

    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, verbose_name="Cidade", null=True, blank=True
    )

    state = models.ForeignKey(
        State,
        verbose_name="Estado",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
