from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoursesConfig(AppConfig):
    name = "apps.courses"
    verbose_name = _("Courses")

    def ready(self):
        try:
            import apps.courses.signals  # noqa F401
        except ImportError:
            pass
