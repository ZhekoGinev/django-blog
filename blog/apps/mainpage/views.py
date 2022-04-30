from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html')