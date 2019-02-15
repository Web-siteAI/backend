from django.db import models
from django.utils.translation import get_language, gettext_lazy as _


# Create your models here.
class Cooperation(models.Model):
    name = models.TextField(verbose_name=_("name"), blank=False, null=False)
    name_en = models.TextField(verbose_name=_("name_en"), blank=False, null=False)

    coop_site = models.URLField(verbose_name=_("coop_site"), max_length=255, blank=True, null=False)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self._get_translation_field('name')

    def _get_translation_field(self, field_name):
        original_field_name = field_name

        lang_code = get_language()

        if lang_code != 'uk':
            field_name = '{}_{}'.format(field_name, lang_code)

        field_value = getattr(self, field_name)

        if field_value:
            return field_value
        else:
            return getattr(self, original_field_name)
