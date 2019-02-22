from django.contrib import admin
from .models import *
# Register your models here.


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/js/tiny_mce.js', '/static/tiny_mce/js/textareas.js',)


admin.site.register(News, TinyMCEAdmin)
admin.site.register(Image)
admin.site.register(Tag)

