from django.contrib import admin
# Register your models here.
from .models import Best


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/js/tiny_mce.js', '/static/tiny_mce/js/textareas.js',)


admin.site.register(Best, TinyMCEAdmin)

