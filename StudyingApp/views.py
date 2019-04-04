from django.shortcuts import render
from MainApp.models import Footer, PageContent, Page
from .models import SubjectBachelor, SubjectType, SubjectMaster


# Create your views here.
def bach(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name_en='Bachelor'))
    page_fields = []
    subject_list = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    subject_type_list = list(SubjectType.objects.all()[:3])
    for i in range(4):
        sub_l = []
        for j in range(2):
            sub_l.append(list(SubjectBachelor.objects.filter(semester=(i * 2 + j + 1))))
        subject_list.append(sub_l)
    content = {"footer_fields": footer_fields, "content_fields": content_fields, "page_fields": page_fields,
               "subject_list": subject_list, "subject_type_list": subject_type_list}
    return render(request, "StudyingApp/bachelor.html", content)


def studying(request):
    footer_fields = Footer.objects.get(pk=1)
    page_fields = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    content = {"footer_fields": footer_fields, "page_fields": page_fields}
    return render(request, "StudyingApp/studying.html", content)


def master(request):
    footer_fields = Footer.objects.get(pk=1)
    content_fields = PageContent.objects.get(page=Page.objects.get(page_name_en='Magister'))
    page_fields = []
    subject_list = []
    for p in list(Page.objects.filter(special_page=False)):
        page_fields.append(PageContent.objects.get(page=p))
    subject_type_list = list(SubjectType.objects.all()[:3])
    for i in range(2):
        sub_l = []
        for j in range(3):
            sub_l.append(list(SubjectMaster.objects.filter(form=i, semester=(j + 1))))
        subject_list.append(sub_l)
    content = {"footer_fields": footer_fields, "content_fields": content_fields, "page_fields": page_fields,
               "subject_list": subject_list, "subject_type_list": subject_type_list}
    return render(request, "StudyingApp/magister.html", content)
