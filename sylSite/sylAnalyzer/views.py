from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def homepage(request):
    if request.method == "GET":
        return render(request, "sylAnalyzer/base_homepage.html")
    elif request.method == "POST":
        return HttpResponseRedirect(reverse("sylAnalyzer:uploaded"))

def details(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def uploaded(request):
    return HttpResponse("Hi")