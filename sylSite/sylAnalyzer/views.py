from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Hello World, you are at the syllabus analyzer homepage.")

def results(request):
    return HttpResponse("Hello again, you are at the results page.")