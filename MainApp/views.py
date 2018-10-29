from django.shortcuts import render


# from django.http import HttpResponse


def index(request):
    return render(request, 'MainApp/homePage.html')


def register(request):
    return render(request, "MainApp/entry.html")

# Create your views here.
