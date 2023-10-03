from django.urls import path
from . import views

app_name = "sylAnalyzer"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("results/", views.results, name="results"),
]