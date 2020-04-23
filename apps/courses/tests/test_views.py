import pytest
from rest_framework import status

from apps.base.test_mixins import GetResponseMixin
from apps.courses.api.views import ListCoursesAPIView, ListLecturesApiView
from .factories import CourseFactory, LectureFactory


class TestListMenuItemsAPIView(GetResponseMixin):
    URL = 'courses:courses'
    VIEW = ListCoursesAPIView

    def test_get_list(self, request_factory):
        self.set_data()
        response = self.get_response(request_factory)
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def set_data():
        [CourseFactory() for i in range(3)]


class TestListLecturesApiView(GetResponseMixin):
    URL = 'courses:lectures-list'
    VIEW = ListLecturesApiView

    def test_get_list(self, request_factory):
        self.set_data()
        response = self.get_response(request_factory)
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def set_data():
        [LectureFactory() for i in range(3)]
