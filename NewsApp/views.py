from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page
from .models import News, Image, Tag
from django.core.paginator import Paginator
# Create your views here.


def news(request, TagIndex):
    footer_fields = Footer.objects.get(pk=1)
    tags_list = Tag.objects.all()
    news_fields = []
    if TagIndex == "all":
        news_fields = News.objects.all()
    else:
        for news in News.objects.all():
            for t in news.tags.all():
                if t.name == TagIndex:
                    news_fields.append(news)
                    break                                         # news_fields = news_fields[(1 - number_page) * 10 - 1: (- number_page) * 10 - 1: -1]
    news_fields = news_fields[::-1]
    paginator = Paginator(news_fields, 7)
    page = request.GET.get('page')
    news_fields = paginator.get_page(page)
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "news_field": news_fields, "tags_list": tags_list, "page_fields": page_fields}
    return render(request, "NewsApp/news.html", content)


def current_news(request, NewsId):
    footer_fields = Footer.objects.get(pk=1)
    cur_news = News.objects.get(pk=int(NewsId))
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    context = {"footer_fields": footer_fields, "current_news": cur_news, "page_fields": page_fields}
    try:
        image_list = Image.objects.filter(news=int(NewsId))
        context["image_list"] = image_list
    except:
        pass
    return render(request, "NewsApp/one_news.html", context)

