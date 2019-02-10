from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<NewsId>', views.current_news, name='current_news'),

]