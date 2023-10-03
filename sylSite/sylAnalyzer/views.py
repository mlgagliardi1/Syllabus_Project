from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "sylAnalyzer/homepage.html")

def details(request):
    return render(request, "sylAnalyzer/details.html")

def examples(request):
    return render(request, "sylAnalyzer/examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/explanation.html")