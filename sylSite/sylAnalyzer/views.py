from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import UploadFileForm

# Create your views here.
def homepage(request):
    uploadFileForm = UploadFileForm()
    context = {
        "upload_form": uploadFileForm,
    }
    return render(request, "sylAnalyzer/base_homepage.html", context)

def uploaderror(request):
    uploadFileForm = UploadFileForm()
    context = {
        "upload_form": uploadFileForm,
        "uploaded": False,
    }
    return render(request, "sylAnalyzer/base_homepage.html", context)

def results(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def uploaded(request):
    #Create the form using models and forms.py
    form = UploadFileForm(request.POST, request.FILES)

    #Check the request is a POST, contains a file, and the form is valid
    if request.method == "POST" and request.FILES['file'] and form.is_valid():
        form.save()
        return redirect("/syllabusanalyzer/results")
    
    else: #form is not valid
        return redirect("/syllabusanalyzer/uploaderror/")
