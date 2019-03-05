from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page
from StudAchievApp.models import Best
# Create your views here.


def best_student(request):
    footer_fields = Footer.objects.get(pk=1)
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    best_fields = list(Best.objects.all())
    content = {"footer_fields": footer_fields, "best_fields": best_fields, "page_fields": page_fields}
    return render(request, "StudAchievApp/best.html", content)
