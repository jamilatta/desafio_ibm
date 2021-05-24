from django import forms as django_forms

# from django.contrib.auth import forms as django_forms
from django.contrib.auth import get_user_model, forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    password = None

    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = (
            "name",
            "email",
            "street",
            "street_number",
            "city",
            "state",
        )
        widgets = {
            "state": django_forms.Select(attrs={"class": "chzn-select"}),
            "city": django_forms.Select(attrs={"class": "chzn-select"}),
        }


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "name",
            "email",
            "street",
            "street_number",
            "city",
            "state",
        )
        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
        widgets = {
            "state": django_forms.Select(attrs={"class": "chzn-select"}),
            "city": django_forms.Select(attrs={"class": "chzn-select"}),
        }
