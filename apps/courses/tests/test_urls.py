from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):

    def test_url_courses_list(self):
        resp = self.client.get(reverse('courses:courses'))
        self.assertEqual(resp.status_code, 200)

    def test_url_lectures_create(self):
        resp = self.client.get(reverse('courses:lecture-create'))
        self.assertEqual(resp.status_code, 200)
