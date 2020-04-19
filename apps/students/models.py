from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from apps.base.utils import custom_uuid


class Student(TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=255,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=255,
    )
    email = models.EmailField(
        _("email address"),
    )

    class Meta:
        db_table = "students"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
