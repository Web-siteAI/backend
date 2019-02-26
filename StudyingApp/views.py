from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page


# Create your views here.
def bach(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name='Bachelor'))
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "content_fields": content_fields, "page_fields": page_fields}
    return render(request, "StudyingApp/bachelor.html", content)


def studying(request):
    footer_fields = Footer.objects.get(pk=1)
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "page_fields": page_fields}
    return render(request, "StudyingApp/studying.html", content)


def magister(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name='Magister'))
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "content_fields": content_fields, "page_fields": page_fields}
    return render(request, "StudyingApp/magister.html", content)
