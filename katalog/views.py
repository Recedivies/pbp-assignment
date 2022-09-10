from django.shortcuts import render
from katalog.models import CatalogItem


def index(request):
    catalog_items = CatalogItem.objects.all()
    context = {
        "catalog_items": catalog_items,
        "name": "Ahmadhi Prananta Hastiputra",
        "student_id": "2106702895",
    }
    return render(request=request, template_name="katalog.html", context=context)
