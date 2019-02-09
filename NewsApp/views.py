from django.shortcuts import render
from MainApp.models import Footer
from .models import News, Images

# Create your views here.


def news(request):
    footer_fields = Footer.objects.get(pk=1)
    news_fields = News.objects.all()
    content = {"footer_fields": footer_fields, "news_field": news_fields}
    return render(request, "NewsApp/news.html", content)


def current_news(request, NewsId):
    footer_fields = Footer.objects.get(pk=1)
    cur_news = News.objects.get(pk=NewsId)
    image_list = []
    for image in Images.objects.all():
        if image.news.id == NewsId:
            image_list.append(image)
    content = {"footer_fields": footer_fields, "current_news": cur_news, "image_list": image_list}
    return render(request, "NewsApp/news.html", content)
