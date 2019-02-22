from django.contrib import admin
from TeachersApp.models import Teacher


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/js/tiny_mce.js', '/static/tiny_mce/js/textareas.js',)


admin.site.register(Teacher, TinyMCEAdmin)

# Register your models here.
