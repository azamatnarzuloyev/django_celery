from django.shortcuts import render
from django.http import HttpResponse
from .tasks import tp1 , tp2 , tp3 , tp4


def home(request):
    tp1.delay(5)
    tp2.delay(5)
    tp3.delay(5)
    return HttpResponse("hello words")