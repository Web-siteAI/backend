from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _
# Create your models here.


class SubjectType(models.Model):
    name = models.CharField(max_length=255, blank=False)
    name_en = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=7, blank=False)

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


class SubjectBachelor(models.Model):
    name = models.CharField(max_length=255, blank=False)
    name_en = models.CharField(max_length=255, blank=False)
    type = models.ForeignKey(SubjectType, on_delete=models.PROTECT)
    CHOICES = [(i, i) for i in range(9) if i is not 0]
    semester = models.IntegerField(choices=CHOICES, default=1, blank=False)
    credit = models.CharField(max_length=5, blank=False)

    def __str__(self):
        return self.get_name() + ' (' + self.type.get_name() + ') ' + self.get_credit()

    def get_credit(self):
        credit_str = str(self.credit) + ' '
        lang_code = get_language()
        if lang_code != 'en':
            credit_str += 'кредит'
            credit_str += 'ів' if float(self.credit) > 4 else 'и'
        else:
            credit_str += 'credits'
        return credit_str

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


class SubjectMaster(models.Model):
    name = models.CharField(max_length=255, blank=False)
    name_en = models.CharField(max_length=255, blank=False)
    type = models.ForeignKey(SubjectType, on_delete=models.PROTECT)
    CHOICES = [(i, i) for i in range(4) if i is not 0]
    semester = models.IntegerField(choices=CHOICES, default=1, blank=False)
    credit = models.CharField(max_length=5, blank=False)
    MASTER_AI = 0
    MASTER_DL_ML = 1
    FORM = (
        (MASTER_AI, "Магістратура (системи штучного інтелекту)"),
        (MASTER_DL_ML, "Магістратура (машинне і глибоке навчання)")
    )
    form = models.IntegerField(choices=FORM, default=MASTER_AI)

    def __str__(self):
        return self.get_name() + ' (' + self.type.get_name() + ') ' + self.get_form_display() + " " + self.get_credit()

    def get_credit(self):
        credit_str = str(self.credit) + ' '
        lang_code = get_language()
        if lang_code != 'en':
            credit_str += 'кредит'
            credit_str += 'ів' if float(self.credit) > 4 else 'и'
        else:
            credit_str += 'credits'
        return credit_str

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
