from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.base.mixins import ActionMixin
from apps.courses.api import docs
from apps.courses.models import Course, CourseParticipant, Lecture
from apps.courses.services import AssignToCourseService, UnAssignFromCourseService, GetStudentsFromCourseService
from apps.students.api.serializers import StudentIdSerializer
from apps.courses.api.serializers import CourseSerializer, CourseParticipantSerializer, LectureSerializer


class ListCoursesAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().participators_count()


class ReadUpdateDeleteCoursesAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().participators_count()


class ListStudentsLearnCoursesAPIView(generics.ListCreateAPIView):
    serializer_class = CourseParticipantSerializer
    queryset = CourseParticipant.objects.all()

    def perform_action(self, serializer):
        GetStudentsFromCourseService(course=self.get_object(), validated_data=serializer.validated_data).execute()


@method_decorator(name='post', decorator=swagger_auto_schema(**docs.course_assign))
class AssignToCourseAPIView(generics.GenericAPIView, ActionMixin):
    serializer_class = StudentIdSerializer
    queryset = Course.objects.all()

    def perform_action(self, serializer):
        AssignToCourseService(course=self.get_object(), validated_data=serializer.validated_data).execute()


@method_decorator(name='post', decorator=swagger_auto_schema(**docs.course_unassign))
class UnAssignCourseAPIView(generics.GenericAPIView, ActionMixin):
    serializer_class = StudentIdSerializer
    queryset = Course.objects.all()

    def perform_action(self, serializer):
        UnAssignFromCourseService(course=self.get_object(), validated_data=serializer.validated_data).execute()


class ListLecturesApiView(generics.ListAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()


class RUDLecturesApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()


class CreateLectureApiView(generics.CreateAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
