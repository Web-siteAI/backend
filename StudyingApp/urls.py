from django.urls import path
from . import views


urlpatterns = [
    path('', views.studying, name="studying"),
    path('bachelor/', views.bach, name="bach"),
    path('magister/', views.master, name="master"),
]
