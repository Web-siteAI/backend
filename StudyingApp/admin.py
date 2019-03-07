from django.contrib import admin
from .models import SubjectType, SubjectBachelor, SubjectMaster
# Register your models here.

admin.site.register(SubjectType)
admin.site.register(SubjectBachelor)
admin.site.register(SubjectMaster)

