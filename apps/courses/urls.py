from django.urls import path

from .api.views import (
    ListCoursesAPIView,
    ReadUpdateDeleteCoursesAPIView,
    ListStudentsLearnCoursesAPIView,
    AssignToCourseAPIView,
    UnAssignCourseAPIView,
    ListLecturesApiView,
    CreateLectureApiView
)

app_name = "courses"

urlpatterns = [
    path("", ListCoursesAPIView.as_view(), name='courses'),
    path("<slug:pk>/", ReadUpdateDeleteCoursesAPIView.as_view(), name='courses-detail'),
    path("<slug:pk>/student/", ListStudentsLearnCoursesAPIView.as_view(), name='student-on-courses'),
    path("<slug:pk>/assign/", AssignToCourseAPIView.as_view(), name="courses-assign"),
    path("<slug:pk>/unassing/", UnAssignCourseAPIView.as_view(), name="course-unassign"),

    path('lectures/', ListLecturesApiView.as_view(), name='lectures-list'),
    path('lectures/<slug:pk>/', ListLecturesApiView.as_view(), name='lecture-update'),
    path('lectures/create/', CreateLectureApiView.as_view(), name='lecture-create')
]
