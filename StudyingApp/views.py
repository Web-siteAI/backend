from django.shortcuts import render
from MainApp.models import Footer, AppContent


# Create your views here.
def bach(request):
    footer_fields = Footer.objects.get(pk=1)
    contents = AppContent.objects.get(pk=1)
    context = {"footer_fields": footer_fields, "contents": contents}
    return render(request, "StudyingApp/bachelor.html", context)


def studying(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "StudyingApp/studying.html", content)


def magister(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "StudyingApp/magister.html", content)
