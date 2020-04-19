from rest_framework import serializers

from apps.students.models import Student


class StudentIdSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Student.objects.all().only('id'),
        required=True
    )


class StudentReportSerializer(serializers.ModelSerializer):
    assigned_courses = serializers.IntegerField(
        default=0,
        read_only=True
    )
    completed_courses = serializers.IntegerField(
        default=0,
        read_only=True
    )

    class Meta:
        model = Student
        fields = ('full_name', 'assigned_courses', 'completed_courses')
