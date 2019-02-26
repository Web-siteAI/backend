from django.contrib import admin
from .models import Partner


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/js/tiny_mce.js', '/static/tiny_mce/js/textareas.js',)


admin.site.register(Partner, TinyMCEAdmin)
# Register your models here.
