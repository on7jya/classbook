from rest_framework import generics

from apps.courses.models import Course
from .serializers import CourseSerializer


class ListCoursesAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().participators_count()
