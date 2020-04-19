from rest_framework import serializers

from apps.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    students_count = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Course
        fields = ('id', 'name', 'start_date', 'end_date', 'students_count')
