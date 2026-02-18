from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("test/", views.test, name="test.html"),
    path("about/", views.about, name="about.html"),
    path("login/", views.login, name="login.html"),
    path("sign-up/", views.sign_up, name="sign-up.html"),
]
