from django.test import TestCase

from apps.courses.models import Course


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Course.objects.create(id=1,
                              name='Python',
                              description='LearnPython',
                              start_date='2020-03-02',
                              end_date='2020-05-31')

    def test_name_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'full name')

    def test_first_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
