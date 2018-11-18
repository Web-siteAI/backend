from django.db import models


class Teacher (models.Model):
    full_name = models.CharField(max_length=255, null=True)
    photo = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%D/", null=True, max_length=255)
    role = models.CharField(max_length=255, null=True)
    orc_id = models.CharField(max_length=40, null=True)
    field_of_work = models.CharField(max_length=255, null=True)
    science_interests = models.CharField(max_length=255, null=True)
    science_researches = models.CharField(max_length=500, null=True)
    interests = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.full_name

# Create your models here.