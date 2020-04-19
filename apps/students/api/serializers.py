from rest_framework import serializers

from apps.students.models import Student


class StudentIdSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Student.objects.all().only('id'),
        required=True
    )
