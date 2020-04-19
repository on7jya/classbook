from django.urls import path

from .api.views import ListCoursesAPIView, ReadUpdateDeleteCoursesAPIView

app_name = "courses"

urlpatterns = [
    path("", ListCoursesAPIView.as_view(), name='courses'),
    path("<slug:pk>/", ReadUpdateDeleteCoursesAPIView.as_view(), name='courses-detail'),
]
