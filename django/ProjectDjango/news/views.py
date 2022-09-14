from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # print(dir(request))
    return HttpResponse('Hello World')

def test(request):
    return HttpResponse('<h1>Test</h1>')