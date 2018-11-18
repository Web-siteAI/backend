from django.shortcuts import render
from TeachersApp.models import Teacher

# from django.http import HttpResponse


def index(request):
    return render(request, 'MainApp/homePage.html')


def mainMethod(request):
    teachers_list = Teacher.objects.all()
    content = {"teachers_list": teachers_list}
    return render(request, "MainApp/mainPage.html", content)

# Create your views here.
