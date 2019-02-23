from django.shortcuts import render
from .models import Footer, PageContent, Page
from TeachersApp.models import Teacher
from ContactApp.models import Contact


def mainMethod(request):
    footer_fields = Footer.objects.get(pk=1)
    teachers_list = Teacher.objects.all()[:4]
    content = {"footer_fields": footer_fields, 'teachers_list':  teachers_list}
    return render(request, "MainApp/mainPage.html", content)


def entrants(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name='Entrance'))
    contact_fields = list(Contact.objects.all())
    content = {"footer_fields": footer_fields, "contact_fields": contact_fields, "content_fields": content_fields}
    return render(request, "MainApp/entrants.html", content)


def excursion(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "MainApp/virtual_tour.html", content)


def newPage(request, PageName):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name=PageName))
    content = {"footer_fields": footer_fields, "content_fields": content_fields}
    return render(request, "MainApp/basic.html", content)
