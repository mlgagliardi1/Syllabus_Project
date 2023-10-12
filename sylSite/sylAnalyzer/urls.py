from django.urls import path
from . import views

app_name = "sylAnalyzer"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("uploaded/", views.uploaded, name="uploaded"),
    path("uploaderror/", views.uploaderror, name="uploaderror"),
    path("results/", views.results, name="results"),
    path("examples/", views.examples, name="examples"),
    path("explanation/", views.explanation, name="explanation"),
]