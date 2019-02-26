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

    admission_location = models.CharField(verbose_name=_("admission_location"), help_text=_("for entrants"),
                                          max_length=255)
    admission_location_en = models.CharField(verbose_name=_("admission_location"),  help_text=_("for entrants"),
                                             max_length=255)

    def get_location(self):
        return self._get_translation_field('location')

    def get_building(self):
        return self._get_translation_field('building')

    def get_site(self):
        return self._get_translation_field('site')

    def get_admission_location(self):
        return self._get_translation_field('admission_location')

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


class Page(models.Model):
    NONE = 0
    DEPARTMENT = 1
    STUDYING = 2
    ACHIEVEMENTS = 3
    OTHER = 4

    INDEX = (
        (NONE, "none"),
        (DEPARTMENT, "about department"),
        (STUDYING, "studying"),
        (ACHIEVEMENTS, "students achievements"),
        (OTHER, "other")
    )
    page_name = models.CharField(max_length=128, blank=False)
    special_page = models.BooleanField(default=False)
    index = models.IntegerField(choices=INDEX, default=NONE)

    def __str__(self):
        return self.page_name + (" special" if self.special_page else "")


class PageContent(models.Model):
    page = models.ForeignKey(Page, blank=False, on_delete=models.PROTECT)
    page_topic = models.CharField(max_length=256, blank=True)
    page_topic_en = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=False)
    text_en = models.TextField(blank=False)

    def __str__(self):
        return self.page.page_name + (" special" if self.page.special_page else "") + " content"

    def get_page_topic(self):
        return self._get_translation_field('page_topic')

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
