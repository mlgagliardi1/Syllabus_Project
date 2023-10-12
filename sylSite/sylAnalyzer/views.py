from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from sylSite.settings import MEDIA_ROOT
from .forms import UploadFileForm
from .core._init_ import _init_
import os

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

        #Delete all prior uploads
        uploadFolder = MEDIA_ROOT + "\\uploads\\"
        for filename in os.listdir(uploadFolder):
            file_path = os.path.join(uploadFolder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print ("Failed to delete %s. Reason %s" % (file_path, e))

        #Save the form to the upload directory    
        form.save()

        #This links to core._init_ where we create the doc object (spacy)     
        _init_(request.FILES['file'].name)
        return redirect("/syllabusanalyzer/results")

    else: #form is not valid
        return redirect("/syllabusanalyzer/uploaderror/")
