from django.shortcuts import render
from TeachersApp.models import Teacher
from .models import Footer


def index(request):
    return render(request, 'MainApp/homePage.html')


def mainMethod(request):
    k = 0
    teachers_list = []
    footer_fields = Footer.objects.get(pk=1)
    for teacher in Teacher.objects.all():
        if k < 4:
            teachers_list.append(teacher)
            k += 1
    content = {"teachers_list": teachers_list, "footer_fields": footer_fields}
    return render(request, "MainApp/mainPage.html", content)


def entrants(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/entrants.html", content)


def science(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/science.html", content)
