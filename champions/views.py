from django.shortcuts import render
from django.http import HttpResponse


def champions(request):
    return HttpResponse("Hello, world. You're at the champions page")
