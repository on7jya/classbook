from rest_framework import serializers

from apps.courses.models import Course, CourseParticipant, Lecture


class CourseSerializer(serializers.ModelSerializer):
    students_count = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Course
        fields = ('id', 'name', 'start_date', 'end_date', 'students_count')


class CourseParticipantSerializer(serializers.ModelSerializer):
    course = CourseSerializer

    class Meta:
        model = CourseParticipant
        fields = ('id', 'course', 'student', 'is_completed')


class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer

    class Meta:
        model = Lecture
        fields = ['name', 'topic', 'course']
