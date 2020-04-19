from django.urls import path

from .api.views import ListCoursesAPIView

app_name = "courses"

urlpatterns = [
    path("", ListCoursesAPIView.as_view(), name='courses'),
]
