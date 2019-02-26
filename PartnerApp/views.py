from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page
from .models import Partner
# Create your views here.


def partner(request):
    footer_fields = Footer.objects.get(pk=1)
    partners_list = Partner.objects.all()
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, 'partners_list': partners_list, "page_fields": page_fields}
    return render(request, "PartnerApp/partner.html", content)
