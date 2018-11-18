from django.shortcuts import render
from TeachersApp.models import Teacher
# from django.http import HttpResponse
from scopus import AuthorRetrieval


def index(request):
    return render(request, 'MainApp/homePage.html')


def mainMethod(request):
    k = 0
    teachers_list = []
    for teacher in Teacher.objects.all():
        if k < 4:
            teachers_list.append(teacher)
    k = 0
    teachers_list = []
    for teacher in Teacher.objects.all():
        if k < 4:
            teachers_list.append(teacher)
    content = {"teachers_list": teachers_list}
    return render(request, "MainApp/mainPage.html", content)

def teachers(request):
    return render(request, "MainApp/teachers.html")

def teacher(request):
    return render(request, "MainApp/teacher.html")

# Create your views here.
