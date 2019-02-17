from django.shortcuts import render
from .models import Footer
from TeachersApp.models import Teacher


def mainMethod(request):
    footer_fields = Footer.objects.get(pk=1)
    teachers_list = Teacher.objects.all()[:4]
    content = {"footer_fields": footer_fields, 'teachers_list':  teachers_list}
    return render(request, "MainApp/mainPage.html", content)


def entrants(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/entrants.html", content)


def science(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/science.html", content)


def excursion(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/excursion.html", content)
