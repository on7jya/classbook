import csv

from django.http import HttpResponse
from rest_framework import generics

from apps.students.models import Student
from .serializers import StudentReportSerializer


class CSVReportAPIView(generics.GenericAPIView):
    serializer_class = StudentReportSerializer
    queryset = Student.objects.all().assigned_courses_count().completed_courses_count()

    def get(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report.csv"'
        header = serializer.Meta.fields
        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        writer.writerow(serializer.data)
        return response
