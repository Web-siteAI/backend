from django.shortcuts import render
from MainApp.models import Footer


def register(request):
    footer_fields = Footer.objects.get(pk=1)
    content = {"footer_fields": footer_fields}
    return render(request, "EntryApp/entry.html", content)

# Create your views here.
