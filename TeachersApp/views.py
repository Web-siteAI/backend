from django.shortcuts import render
from .models import Teacher


def teachers(request):
    teachers_list = Teacher.objects.all()
    content = {"teachers_list": teachers_list}
    return render(request, "TeachersApp/teachers.html", content)


def getTeacher(request, TeacherId):
    teacher = Teacher.objects.get(pk=int(TeacherId))
    content = {"teacher": teacher}
    return render(request, "TeachersApp/teacher.html", content)


# Create your views here.
