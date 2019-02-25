from django.shortcuts import render
from MainApp.models import Footer
from .models import Contact
# Create your views here.


def contacts(request):
    footer_fields = Footer.objects.get(pk=1)
    contact_fields = list(Contact.objects.filter(selection_committee=False))
    content = {"footer_fields": footer_fields, "contact_fields": contact_fields}
    return render(request, "ContactApp/contact.html", content)
