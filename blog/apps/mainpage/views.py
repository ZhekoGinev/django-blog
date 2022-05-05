from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def index(request):
    return render(request, "mainpage/index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    articles = Article.objects.all().order_by('-created_on')
    return render(request, "articles.html", {'articles' : articles})


def contact(request):
    return render(request, "contact.html")


def article_details(request, slug):
    context = Article.objects.get(slug=slug)
    return render(request, 'article-details.html', {'context': context})