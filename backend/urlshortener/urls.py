from django.urls import path

from .views import ShortenURLView

urlpatterns = [
    path("v1", ShortenURLView.as_view({"post": "shorten_url"})),
    path("v1/<str:short_url>", ShortenURLView.as_view({"get": "get_orginal_url"})),
]
