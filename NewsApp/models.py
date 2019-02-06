from django.db import models
from datetime import date
from django.utils.translation import get_language, ugettext_lazy as _


# Create your models here
class News(models.Model):
    topic = models.CharField(max_length=255, blank=False, null=False)
    topic_en = models.CharField(max_length=255, blank=False, null=False)

    short_description = models.TextField(blank=True, null=False)
    short_description_en = models.TextField(blank=True, null=False)

    post = models.TextField(blank=False, null=False)
    post_en = models.TextField(blank=False, null=False)

    data_post = models.DateField(default=date.today)

    photo = models.ImageField(max_length=255, upload_to="pictures/%Y/%m/%D/", blank=True, null=True)

    def __str__(self):
        return self.get_topic()

    def get_topic(self):
        return self._get_translation_field('topic')

    def get_short_description(self):
        return self._get_translation_field('short_description')

    def get_post(self):
        return self._get_translation_field('post')

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
