from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentsConfig(AppConfig):
    name = "apps.students"
    verbose_name = _("Students")

    def ready(self):
        try:
            import apps.students.signals  # noqa F401
        except ImportError:
            pass
