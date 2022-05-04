from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def index(request):
    return render(request, "mainpage/index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    return render(request, "articles.html")


def contact(request):
    return render(request, "contact.html")
