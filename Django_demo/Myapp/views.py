from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    msg = "hello"
    return HttpResponse(msg)