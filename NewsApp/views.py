from django.shortcuts import render
from MainApp.models import Footer
from .models import News


def news(request):
    footer_fields = Footer.objects.get(pk=1)
    news_fields = News.objects.all()
    content = {"footer_fields": footer_fields, "news_field": news_fields}
    return render(request, "NewsApp/news.html", content)

# Create your views here.
