from django.shortcuts import render


# from django.http import HttpResponse


def index(request):
    return render(request, 'MainApp/homePage.html')


def register(request):
    return render(request, "MainApp/entry.html")

def mainMethod(request):
    return render(request, "MainApp/mainPage.html")

def teachers(request):
    return render(request, "MainApp/teachers.html")
# Create your views here.
