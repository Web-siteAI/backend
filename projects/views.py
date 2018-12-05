from django.shortcuts import render
from MainApp.models import Footer


def projects(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, 'projects/projects.html', content)
