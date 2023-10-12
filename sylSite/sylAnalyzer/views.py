from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import UploadFileForm
from .core.saveFile import saveFile

# Create your views here.

def homepage(request):
    return render(request, "sylAnalyzer/base_homepage.html")

def results(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def uploaded(request):
    #Create the form using forms.py
    form = UploadFileForm(request.POST, request.FILES)
    #Check the request is a POST and contains a file
    if request.method == "POST" and request.FILES['file']:
        #Create the uploadedFile var and pass it to saveFile. If file saved properly, redirect to results, else redirect to homepage
        uploadedFile = request.FILES['file']
        if saveFile(uploadedFile):
            return redirect("/syllabusanalyzer/results")
        else:
            print("File Not Saved")
            return HttpResponse("not uploaded")
    else:
        form = UploadFileForm()
        return HttpResponse("Form Invalid")