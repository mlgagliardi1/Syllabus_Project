from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .core.docCreation import test

# Create your views here.

def homepage(request):
    if request.method == "GET":
        return render(request, "sylAnalyzer/base_homepage.html")
    
    #Currently, the HTML will send the form and it is received
    #Now, we need to create an external method to validate and handle file input
    #And redirect the user to an "uploaded" page.
    #Currently, the uploaded form reads as invalid

    elif request.method == "POST" and request.FILES['uploadedFile']:
            form = UploadFileForm(request.POST, request.FILES)
            #This line prints file to show if it uploaded or not
            print(form.errors)

            uploaded_file = request.FILES['uploadedFile']
            fs = FileSystemStorage()
            filename = fs.save(uploadedFile.name, uploadedFile)
            uploaded_file_url = fs.url(filename)
            
            return HttpResponse("uploaded")
    else:
            form = UploadFileForm()
            return HttpResponse("Form Invalid")
            
def details(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def uploaded(request):
    return HttpResponse("hey there")