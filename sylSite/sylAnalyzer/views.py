from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "sylAnalyzer/base_homepage.html")

def details(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")
