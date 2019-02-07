from django.shortcuts import render
from .models import Footer
from TeachersApp.models import Teacher


def mainMethod(request):
    teachers_list = []
    footer_fields = Footer.objects.get(pk=1)
    k = 0
    for teacher in Teacher.objects.all():
        if k < 4:
            teachers_list.append(teacher)
            k += 1
    content = {"footer_fields": footer_fields, ' teachers_list':  teachers_list}
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


def bach(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/bachelor.html", content)


def navch(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/navch.html", content)


def magister(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/magister.html", content)
