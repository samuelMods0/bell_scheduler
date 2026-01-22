from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    with open("main/scources/index.html", "r") as f:
        index_file = f.read()
    return HttpResponse(index_file)

def test(response):
    with open("main/scources/test.html", "r") as f:
        test_file = f.read()
    return HttpResponse(test_file)
