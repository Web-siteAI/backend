from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page


def projectsOfStudents(request):
    return render(request, 'ProjectsApp/ProjectsApp.html')


def projectsOfDepartment(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, 'ProjectsApp/ProjectsApp.html', content)

