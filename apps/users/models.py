from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from apps.base.utils import custom_uuid


class User(AbstractUser, TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    # First Name and Last Name do not cover name patterns around the globe.
    name = models.CharField(
        _("Name of User"),
        blank=True,
        max_length=255
    )

    class Meta:
        db_table = 'users'
