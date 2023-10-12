from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import UploadFileForm

# Create your views here.

def homepage(request):
    uploadFileForm = {}
    uploadFileForm['form'] = UploadFileForm()
    return render(request, "sylAnalyzer/base_homepage.html", uploadFileForm)

def results(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def uploaded(request):
    #Create the form using models and forms.py
    form = UploadFileForm(request.POST, request.FILES)
    #Check the request is a POST and contains a file
    if request.method == "POST" and request.FILES['file'] and form.is_valid():
        #Create the uploadedFile var and pass it to saveFile. If file saved properly, redirect to results, else redirect to homepage
        form.save()
        return redirect("/syllabusanalyzer/results")
    else:
        form = UploadFileForm()
        return redirect("/syllabusanalyzer/")
