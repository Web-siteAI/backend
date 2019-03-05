"""AIWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainMethod, name='mainMethod'),

    path('entrants/', views.entrants, name="entrants"),
    path('virtual-tour/', views.excursion, name="excursion"),

    path('studying/', include("StudyingApp.urls")),
    path('teachers/', include("TeachersApp.urls")),
    path('projects/', include("ProjectsApp.urls")),
    path('cooperation/', include("CooperationApp.urls")),
    path('news/', include("NewsApp.urls")),
    path('contacts/', include("ContactApp.urls")),
    path('partners/', include("PartnerApp.urls")),
    path('p/<PageName>/', views.newPage, name="<PageName>")
]



