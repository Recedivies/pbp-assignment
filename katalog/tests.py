from django.urls import reverse
from django.test import TestCase
from katalog.models import CatalogItem


class CatalogViewTests(TestCase):
    def test_url_exists(self):
        response = self.client.get("/katalog/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("katalog"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("katalog"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "katalog.html")


class CatalogModelTests(TestCase):
    def test_create_catalog(self):
        catalog = CatalogItem.objects.create(
            item_name="Samsung Galaxy S22",
            item_price=12249000,
            description="Specification: Snapdragon 8",
            item_stock=1,
            rating=5,
            item_url="https://www.tokopedia.com/mhi-samsung/samsung-galaxy-s22-8-256gb-black",
        )
        self.assertEqual(
            CatalogItem.objects.get(item_name="Samsung Galaxy S22"), catalog
        )
