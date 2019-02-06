from django.contrib import admin
from .models import Footer
# Register your models here.
#admin.site.register(Footer) #, FooterAdmin)


@admin.register(Footer)
class ExampleModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Footer.objects.exists():
            retVal = False
        return retVal

# from django.conf import settings
# from django.db import models
# from translations.admin import TranslatableAdmin, TranslationInline


# class FooterAdmin(TranslatableAdmin):
#     inlines = [TranslationInline]
# class FooterTranslationInlineAdmin(admin.StackedInline):
#     verbose_name = "Translation"
#     verbose_name_plural = "Translations"
#     model = FooterTranslation
#     max_num = len(settings.LANGUAGES)
#     extra = 1
#
#
# class FooterAdmin(admin.ModelAdmin):
#     inlines = [FooterTranslationInlineAdmin,]



