from django.urls import path
from . import views

app_name = "sylAnalyzer"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("details/", views.details, name="details"),
    path("examples/", views.examples, name="examples"),
    path("explanation/", views.explanation, name="explanation"),
]