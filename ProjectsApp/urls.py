from django.urls import path, include
from . import views

urlpatterns = [
    path('student/', views.projectsOfStudents, name='projectsStud'),
    path('department/', views.projectsOfDepartment, name='projectsDept'),
]