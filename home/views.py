from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "base/home.html")

def about(request):
    return render(request, "base/about.html")

def process(request):
    return render(request, "base/process.html")

def blog(request):
    return render(request, "base/blog.html")

def login(request):
    return render(request, "base/login.html")
 
