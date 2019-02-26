from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _
# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    description_en = models.TextField(blank=False)
    site = models.URLField(blank=True)
    icon = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%D/")

    def __str__(self):
        return self.name

    def get_description(self):
        return self._get_translation_field('description')

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
