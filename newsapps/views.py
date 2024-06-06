from django.shortcuts import render
from django.http import HttpResponse
from .tasks import task1


def home(request):
    task1.delay(5)
    return HttpResponse("hello words")