from django.urls import path, include
from . import views

urlpatterns = [
    path('<TagIndex>/<NumberPage>/', views.news, name='news'),
    path('id/<NewsId>/', views.current_news, name='current_news'),

]