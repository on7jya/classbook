from django.contrib import admin
from .models import Course, CourseParticipant, Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(CourseParticipant)
class CourseParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "student"]


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "topic", "course"]
    search_fields = ["name"]
