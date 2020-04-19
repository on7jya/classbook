from django.contrib import admin
from .models import Course, CourseParticipant


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(CourseParticipant)
class CourseParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "student"]
