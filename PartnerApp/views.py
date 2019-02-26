from django.shortcuts import render
from MainApp.models import Footer
from .models import Partner
# Create your views here.


def partner(request):
    footer_fields = Footer.objects.get(pk=1)
    partners_list = Partner.objects.all()
    content = {"footer_fields": footer_fields, 'partners_list': partners_list}
    return render(request, "PartnerApp/partner.html", content)
