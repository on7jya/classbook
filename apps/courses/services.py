from .models import CourseParticipant
from .api.exceptions import AlreadyAssigned, AlreadyUnAssigned


class AssignToCourseService:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        obj, created = CourseParticipant.objects.get_or_create(course=self.course, student=self.student)
        if not created:
            raise AlreadyAssigned()


class UnAssignFromCourseService:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        obj, created = CourseParticipant.objects.filter(course=self.course, student=self.student).delete()
        if not created:
            raise AlreadyUnAssigned()


class GetStudentsFromCourseService:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        CourseParticipant.objects.get_or_create(course=self.course, student=self.student)
