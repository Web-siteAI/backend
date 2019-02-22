from django.db import models
from django.utils.translation import get_language, gettext_lazy as _


class Footer(models.Model):
    email = models.EmailField(verbose_name=_("email"))

    phone_number = models.CharField(verbose_name=_("phone_number"), max_length=20)

    location = models.CharField(verbose_name=_("location"), max_length=255)
    location_en = models.CharField(verbose_name=_("location_en"), max_length=255)

    building = models.CharField(verbose_name=_("building"), max_length=255)
    building_en = models.CharField(verbose_name=_("building_en"), max_length=255)

    social_net = models.CharField(verbose_name=_("social_net"), max_length=255)
    social_net_url = models.URLField(verbose_name=_("social_net_url"), max_length=255)

    site = models.CharField(verbose_name=_("site"), max_length=255)
    site_en = models.CharField(verbose_name=_("site_en"), max_length=255)
    site_url = models.URLField(verbose_name=_("site_url"), max_length=255)

    def get_location(self):
        return self._get_translation_field('location')

    def get_building(self):
        return self._get_translation_field('building')

    def get_site(self):
        return self._get_translation_field('site')

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


class AppContent(models.Model):
    app_name = models.CharField(max_length=128, blank=False)
    app_topic = models.CharField(max_length=128, blank=True)
    app_topic_en = models.CharField(max_length=128, blank=True)
    text = models.TextField(blank=False)
    text_en = models.TextField(blank=False)

    def __str__(self):
        return self.app_name

    def get_app_topic(self):
        return self._get_translation_field('app_topic')

    def get_text(self):
        return self._get_translation_field('text')

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
