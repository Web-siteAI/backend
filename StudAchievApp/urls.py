from django.urls import path, include
from . import views

urlpatterns = [
    path('bests/', views.best_student, name="best_student")
]