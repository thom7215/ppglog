from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>PPG Log Home</h1>')


def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')
