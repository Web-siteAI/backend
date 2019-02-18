from django.urls import path, include
from . import views

urlpatterns = [
    path('<TagIndex>/', views.news, name='news'),
   # path('<TagIndex>/<NumberPage>/<Comand>/', views.news_switch, name='news_switch'),
    path('id/<NewsId>/', views.current_news, name='current_news'),

]