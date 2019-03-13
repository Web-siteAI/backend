from django.db import models
from datetime import date
from django.utils.translation import get_language, ugettext_lazy as _


# Create your models here
class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    name_uk = models.CharField(max_length=255, blank=False, null=False)
    color = models.CharField(max_length=7, blank=False)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self._get_translation_field('name')

    def _get_translation_field(self, field_name):
        original_field_name = field_name

        lang_code = get_language()

        if lang_code != 'en':
            field_name = '{}_{}'.format(field_name, lang_code)

        field_value = getattr(self, field_name)

        if field_value:
            return field_value
        else:
            return getattr(self, original_field_name)


class News(models.Model):
    topic = models.CharField(verbose_name=_("topic"), max_length=255, blank=False, null=False)
    topic_en = models.CharField(verbose_name=_("topic_en"), max_length=255, blank=False, null=False)

    short_description = models.TextField(
        verbose_name=_("short_description"), max_length=500, blank=True, null=False)
    short_description_en = models.TextField(
        verbose_name=_("short_description_en"), max_length=500, blank=True, null=False)

    post = models.TextField(verbose_name=_("post"), blank=False, null=False)
    post_en = models.TextField(verbose_name=_("post_en"), blank=False, null=False)

    data_post = models.DateField(verbose_name=_("data_post"), default=date.today, null=False)

    photo = models.ImageField(
        verbose_name=_("photo"), help_text=_("Use ImagesForm if you want to add more than one image"),
        max_length=255, upload_to="pictures/%Y/%m/%D/", blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:

        ordering = ["data_post"]

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


class Image(models.Model):
    news = models.ForeignKey(News, related_name="news", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pictures/%Y/%m/%D/", blank=False, null=False)
    image_name = models.CharField(max_length=255, default="", blank=True, null=False)

    def __str__(self):
        return self.news.get_topic() + " (" + self.get_name_of_image() + ")"

    def get_name_of_image(self):
        if self.image_name != "":
            img_name = str(self.image_name)
        else:
            string = str(self.image)
            img_name = string[(string.rfind("/") + 1):string.find(".")]
        return img_name




