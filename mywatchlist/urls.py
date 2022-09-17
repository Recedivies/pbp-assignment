from django.urls import path
from mywatchlist.views import show_html, show_xml, show_json

urlpatterns = [
    path("html", view=show_html, name="show_html"),
    path("xml", view=show_xml, name="show_xml"),
    path("json", view=show_json, name="show_json"),
]
