from django.urls import path

from apps.students.api.views import CSVReportAPIView

app_name = "students"
urlpatterns = [
    path("<slug:pk>/csv-report/", CSVReportAPIView.as_view(), name='csv_report'),
]
