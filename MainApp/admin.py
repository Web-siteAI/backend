from django.contrib import admin
from .models import Footer, PageContent, Page
from django.conf import settings
# Register your models here.


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tiny_mce/js/tiny_mce.js', '/static/tiny_mce/js/textareas.js',)


admin.site.register(PageContent, TinyMCEAdmin)
admin.site.register(Page)


@admin.register(Footer)
class ExampleModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Footer.objects.exists():
            retVal = False
        return retVal


# Create your views here.
def switch_lang_code(path, language):
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]

    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)

    # Split the parts of the path
    parts = path.split('/')

    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = "/" + language

    # Return the full new path
    return '/'.join(parts)



