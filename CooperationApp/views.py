from django.shortcuts import render
from MainApp.models import Footer, Page, PageContent
from .models import Cooperation

# Create your views here.


def cooperation(request):
    footer_fields = Footer.objects.get(pk=1)
    coop = Cooperation.objects.all()
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "coop": coop, "page_fields": page_fields}
    return render(request, "CooperationApp/cooperation.html", content)
