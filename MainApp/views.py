from django.shortcuts import render
from TeachersApp.models import Teacher

def index(request):
    return render(request, 'MainApp/homePage.html')


def mainMethod(request):
    k = 0
    teachers_list = []
    for teacher in Teacher.objects.all():
        if k < 4:
            teachers_list.append(teacher)
            k += 1
    content = {"teachers_list": teachers_list}
    return render(request, "MainApp/mainPage.html", content)

def entrants(request):
    return render(request, "MainApp/entrants.html")

def science(request):
    return render(request, "MainApp/science.html")