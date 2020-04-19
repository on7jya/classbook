from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.base.mixins import ActionMixin
from apps.courses.api import docs
from apps.courses.models import Course, CourseParticipant
from apps.students.api.serializers import StudentIdSerializer
from apps.courses.api.serializers import CourseSerializer


class ListCoursesAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().participators_count()


class ReadUpdateDeleteCoursesAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().participators_count()


@method_decorator(name='post', decorator=swagger_auto_schema(**docs.course_assign))
class AssignToCourseAPIView(generics.GenericAPIView, ActionMixin):
    serializer_class = StudentIdSerializer
    queryset = Course.objects.all()

    def perform_action(self, serializer):
        CourseParticipant.objects.get_or_create(course=self.get_object(), student=serializer.validated_data['student'])


@method_decorator(name='post', decorator=swagger_auto_schema(**docs.course_unassign))
class UnAssignCourseAPIView(generics.GenericAPIView, ActionMixin):
    serializer_class = StudentIdSerializer
    queryset = Course.objects.all()

    def perform_action(self, serializer):
        CourseParticipant.objects.filter(
            course=self.get_object(), student=serializer.validated_data['student']).delete()
