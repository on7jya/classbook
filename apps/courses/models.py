from django.db import models
from django_extensions.db.models import TimeStampedModel
from apps.base.utils import custom_uuid
from django.utils.translation import gettext_lazy as _


class Course(TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    name = models.CharField(
        _("full name"),
        max_length=255,
    )
    description = models.TextField(
        _("description"),
        max_length=3000,
        blank=True
    )
    start_date = models.DateField(
        _("start date"),
        null=True,
        blank=True,
    )
    end_date = models.DateField(
        _("end date"),
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name[:80]


class CourseParticipant(TimeStampedModel):
    course = models.ForeignKey(
        'courses.Course',
        related_name='participants_set',
        null=True,
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        'students.Student',
        related_name='courses_set',
        null=True,
        on_delete=models.SET_NULL,
    )
    is_completed = models.BooleanField(
        _("is completed"),
        default=False
    )

    class Meta:
        db_table = 'course_participants'
        unique_together = ["course", "student"]

    def __str__(self):
        return f"{self.student} participate in {self.course}"
