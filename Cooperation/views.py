from django.shortcuts import render
from MainApp.models import Footer
from .models import Cooperation

# Create your views here.


def cooperation(request):
    footer_fields = Footer.objects.get(pk=1)
    coop = Cooperation.objects.all()

    content = {"footer_fields": footer_fields, "coop": coop}
    return render(request, "MainApp/cooperation.html", content)
