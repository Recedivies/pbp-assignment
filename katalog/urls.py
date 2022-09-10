from django.urls import path
from katalog.views import index


urlpatterns = [
    path(route="", view=index, name="katalog"),
]
