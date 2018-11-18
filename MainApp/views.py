from django.shortcuts import render
from django.http import HttpResponse

# from django.http import HttpResponse

def index(request):
    return render(request, 'MainApp/homePage.html')

from scopus import AuthorRetrieval

def register(request):
    return render(request, "MainApp/entry.html")

def mainMethod(request):
    s = AuthorRetrieval(57198358655)
    print(s)
    return render(request, "MainApp/mainPage.html")

def teachers(request):
    return render(request, "MainApp/teachers.html")

def teacher(request):
    return render(request, "MainApp/teacher.html")


# Create your views here.
