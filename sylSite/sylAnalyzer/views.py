from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def homepage(request):
    return render(request, "sylAnalyzer/base_homepage.html")

def details(request):
    return render(request, "sylAnalyzer/base_details.html")

def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")

def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")

def simple_upload(request):
    if request.method == 'POST' and request.FIELS['myfile']:
        myfile = request.FILES['myfiles']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return HttpResponse("file uploaded successfully?")