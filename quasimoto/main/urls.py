from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("test/", views.test, name="test.html"),
]
