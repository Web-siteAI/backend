from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _


# Create your models here.
class Teacher (models.Model):
    full_name = models.CharField(help_text="Прізвище Ім'я По-батькові", max_length=255, null=False)
    full_name_en = models.CharField(help_text="Last name Name Surname", max_length=255, null=False)

    photo = models.ImageField(max_length=255, blank=True, upload_to="pictures/%Y/%m/%D/", null=False)

    role = models.CharField(max_length=255, blank=False, null=False)
    role_en = models.CharField(max_length=255, null=False)

    field_of_work = models.CharField(max_length=255, blank=True, null=False)
    field_of_work_en = models.CharField(max_length=255, blank=True, null=False)

    science_interests = models.CharField(max_length=255, blank=True, null=False)
    science_interests_en = models.CharField(max_length=255, blank=True, null=False)

    science_researches = models.CharField(max_length=500, blank=True, null=False)
    science_researches_en = models.CharField(max_length=500, blank=True, null=False)

    interests = models.TextField(max_length=500, blank=True, null=False)
    interests_en = models.TextField(max_length=500, blank=True, null=False)

    description = models.TextField(blank=True, null=False)
    description_en = models.TextField(blank=True, null=False)

    scopus_id = models.IntegerField(default=0, null=False)

    scopus_orcid = models.CharField(max_length=100, default=" ", blank=True, null=False)

    scopus_hindex = models.IntegerField(default='0', null=False)

    scopus_documents = models.IntegerField(default='0', null=False)

    scopus_citations = models.IntegerField(default='0', null=False)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self._get_translation_field('full_name')

    def get_role(self):
        return self._get_translation_field('role')

    def get_field_of_work(self):
        return self._get_translation_field('field_of_work')

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
