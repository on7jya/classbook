from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):

    def test_url_courses_list(self):
        resp = self.client.get(reverse('courses:courses'))
        self.assertEqual(resp.status_code, 200)
