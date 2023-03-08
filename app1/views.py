from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sachin(request):
    return HttpResponse('<h1><marquee>Sachin is god of cricker</h1></marquee>')

