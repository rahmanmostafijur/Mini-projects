from django.urls import path

from .views import home, shorten_url

urlpatterns = [
    path("", home, name="home"),
    path("shorten/", shorten_url, name="shorten_url"),
]
