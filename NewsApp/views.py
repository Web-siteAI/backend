from django.shortcuts import render
from MainApp.models import Footer
from .models import News, Image, Tag

# Create your views here.


def news(request, NumberPage, TagIndex):
    number_page = int(NumberPage)
    footer_fields = Footer.objects.get(pk=1)
    news_fields = []
    if TagIndex == "all":
        news_fields = News.objects.all()[(number_page-1)*10:number_page*10]
    else:
        for news in News.objects.all():
            for t in news.tags.all():
                if t.name == TagIndex:
                    news_fields.append(news)
                    break
        news_fields = news_fields[(number_page - 1) * 10:number_page * 10]
    tags_list = Tag.objects.all()
    content = {"footer_fields": footer_fields, "news_field": news_fields, "tags_list": tags_list}
    return render(request, "NewsApp/news.html", content)


def current_news(request, NewsId):
    footer_fields = Footer.objects.get(pk=1)
    cur_news = News.objects.get(pk=int(NewsId))
    image_list = Image.objects.filter(news.id == NewsId)
    content = {"footer_fields": footer_fields, "current_news": cur_news, "image_list": image_list}
    return render(request, "NewsApp/news.html", content)
