from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
# Create your models here.


class Best(models.Model):
    image = models.ImageField(upload_to="pictures/%Y/%m/%D/", blank=True, null=False)
    image_name = models.CharField(max_length=255, default="", blank=True, null=False)
    course = models.CharField(max_length=255, default="", blank=False, null=False)
    student = models.TextField()

    def __str__(self):
        return self.course + " students"
