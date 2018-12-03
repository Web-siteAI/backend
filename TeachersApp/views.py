from django.shortcuts import render
from .models import Teacher
import os
import requests
from bs4 import BeautifulSoup


def teachers(request):
    teachers_list = Teacher.objects.all()
    content = {"teachers_list": teachers_list}
    return render(request, "TeachersApp/teachers.html", content)


def getTeacher(request, TeacherId):
    id = int(TeacherId)
    url = "http://ena.lp.edu.ua/simple-search?location=%2F&query=" + 'кривенчук+юрій' + " &rpp=10&sort_by=score&order=desc"
    r = requests.get(url)
    with open('./static/teachers/all/%d.html' % (2222), 'w') as output_file:
        output_file.write(r.text.encode('utf8', 'ignore').decode('utf8', 'ignore'))

    id = int(TeacherId)
    orcid = " "
    hindex = 0
    docs = 0
    if id > 1000:
        if os.path.isfile("./static/teachers/all/%d.html"%(id)):
            k = 1
        else:
            url = 'https://www.scopus.com/authid/detail.uri?authorId=%d' % (id)
            r = requests.get(url)
            with open('./static/teachers/all/%d.html' % (id), 'w') as output_file:
                output_file.write(r.text.encode('cp1251', 'ignore').decode('utf8', 'ignore'))
            soup = BeautifulSoup(open("./static/teachers/all/%d.html" % (id)), "html.parser")

            orcids = soup.findAll("span", class_="anchorText")


            for o in orcids:
                if o.getText()[0:4] == "http":
                    orcid = o.getText()



            hd = soup.findAll("span", class_="fontLarge")
            hindex = int(hd[0].getText())
            docs = int(hd[1].getText())

            teachers = Teacher.objects.filter(scopus_id="%d" % (id));
            teacher = teachers[0]
            teacher.scopus_orcid = orcid
            teacher.scopus_hindex = hindex
            teacher.scopus_documents = docs
            teacher.save()

        teachers = Teacher.objects.filter(scopus_id = "%d" % (id));
        teacher = teachers[0]


        content = {"teacher": teacher}
        return render(request, "TeachersApp/teacher.html", content)
    else:
        teacher = Teacher.objects.get(pk=id)
        content = {"teacher": teacher}


        return render(request, "TeachersApp/teacher.html", content)
# Create your views here.
