from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return render(response, 'main/index.html')


def test(response):
    return render(response, 'main/test.html')


def about(response):
    return render(response, 'main/about.html')


def login(response):
    return render(response, 'main/login.html')


def sign_up(response):
    return render(response, 'main/sign-up.html')

def base_test(response):

    return render(response, "main/base_test.html", {})
