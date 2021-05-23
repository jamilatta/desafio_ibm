from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "desafio_ibm.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import desafio_ibm.users.signals  # noqa F401
        except ImportError:
            pass
