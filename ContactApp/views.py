from django.shortcuts import render
from MainApp.models import Footer, Page, PageContent
from .models import Contact
# Create your views here.


def contacts(request):
    footer_fields = Footer.objects.get(pk=1)
    contact_fields = list(Contact.objects.all())
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "contact_fields": contact_fields, "page_fields": page_fields}
    return render(request, "ContactApp/contact.html", content)
