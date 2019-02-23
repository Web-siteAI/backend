from django.shortcuts import render
from MainApp.models import Footer, PageContent


# Create your views here.
def bach(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(pk=1)
    content = {"footer_fields": footer_fields, "content_fields": content_fields}
    return render(request, "StudyingApp/bachelor.html", content)


def studying(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "StudyingApp/studying.html", content)


def magister(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(pk=3)
    content = {"footer_fields": footer_fields, "content_fields": content_fields}
    return render(request, "StudyingApp/magister.html", content)
