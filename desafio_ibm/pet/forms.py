from django import forms

from . import models


class PetForm(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ("name", "race", "age", "weight", "category", "city")

        widgets = {
            "category": forms.Select(attrs={"class": "chzn-select form-control"}),
            "city": forms.Select(attrs={"class": "chzn-select form-control"}),
        }
