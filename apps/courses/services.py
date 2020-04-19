from .models import CourseParticipant


class AssignToCourseService:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        CourseParticipant.objects.get_or_create(course=self.course, student=self.student)


class UnAssignFromCourseService:
    def __init__(self, course, validated_data):
        self.course = course
        self.student = validated_data['student']

    def execute(self):
        CourseParticipant.objects.filter(course=self.course, student=self.student).delete()
