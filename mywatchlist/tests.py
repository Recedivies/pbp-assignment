from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class MyWatchListTests(TestCase):
    def test_show_html_url(self):
        response = self.client.get(reverse("show_html"))
        self.assertEqual(response.status_code, 200)

    def test_show_xml_url(self):
        response = self.client.get(reverse("show_xml"))
        self.assertEqual(response.status_code, 200)

    def test_show_json_url(self):
        response = self.client.get(reverse("show_json"))
        self.assertEqual(response.status_code, 200)
