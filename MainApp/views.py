from django.shortcuts import render
from .models import Footer, AppContent
from TeachersApp.models import Teacher
from ContactApp.models import Contact


def mainMethod(request):
    footer_fields = Footer.objects.get(pk=1)
    teachers_list = Teacher.objects.all()[:4]
    content = {"footer_fields": footer_fields, 'teachers_list':  teachers_list}
    return render(request, "MainApp/mainPage.html", content)


def entrants(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = AppContent.objects.get(pk=2)
    contact_fields = list(Contact.objects.all())
    content = {"footer_fields": footer_fields, "contact_fields": contact_fields, "content_fields": content_fields}
    return render(request, "MainApp/entrants.html", content)


def science(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/science.html", content)


def excursion(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/virtual_tour.html", content)
