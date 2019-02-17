from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _


# Create your models here.
class Teacher (models.Model):
    full_name = models.CharField(
        verbose_name=_("full_name"), help_text="Прізвище Ім'я По-батькові", max_length=255, null=False)
    full_name_en = models.CharField(
        verbose_name=_("full_name_en"), help_text="Last name Name Surname", max_length=255, null=False)

    photo = models.ImageField(max_length=255, blank=True, upload_to="pictures/%Y/%m/%D/", null=True)

    role = models.CharField(verbose_name=_("role"), max_length=255, default="", null=False)
    role_en = models.CharField(verbose_name=_("role_en"), max_length=255, default="", null=False)

    scientific_rank = models.CharField(
        verbose_name=_("scientific_rank"), max_length=255, default="", blank=False, null=False)
    scientific_rank_en = models.CharField(
        verbose_name=_("scientific_rank_en"), max_length=255, default=" ", blank=False, null=False)

    academic_site = models.URLField(verbose_name=_("academic_site"), max_length=255, blank=True)

    science_interests = models.CharField(
        verbose_name=_("science_interests"), max_length=500, blank=True, null=False)
    science_interests_en = models.CharField(
        verbose_name=_("science_interests_en"), max_length=500, blank=True, null=False)

    science_researches = models.TextField(
        verbose_name=_("science_researches"), max_length=1000, blank=True, null=False)
    science_researches_en = models.TextField(
        verbose_name=_("science_researches_en"), max_length=1000, blank=True, null=False)

    interests = models.TextField(verbose_name=_("interests"), max_length=500, blank=True, null=False)
    interests_en = models.TextField(verbose_name=_("interests_en"), max_length=500, blank=True, null=False)

    description = models.TextField(verbose_name=_("description"), blank=True, null=False)
    description_en = models.TextField(verbose_name=_("description_en"), blank=True, null=False)

    scopus_id = models.IntegerField(default=0, null=False)

    scopus_orcid = models.CharField(max_length=100, default=" ", blank=True, null=False)

    scopus_hindex = models.IntegerField(default='0', null=False)

    scopus_documents = models.IntegerField(verbose_name=_("scopus_documents"), default='0', null=False)

    scopus_citations = models.IntegerField(verbose_name=_("scopus_citations"), default='0', null=False)

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self._get_translation_field('full_name')

    def get_scientific_rank(self):
        return self._get_translation_field('scientific_rank')

    def get_role(self):
        return self._get_translation_field('role')

    def get_science_interests(self):
        return self._get_translation_field('science_interests')

    def get_science_researches(self):
        return self._get_translation_field('science_researches')

    def get_interests(self):
        return self._get_translation_field('interests')

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
