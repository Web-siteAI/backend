from django.db import models


class Teacher (models.Model):
    full_name = models.CharField(max_length=255)
    # photo = models.ImageField()
    role = models.CharField(max_length=255)
    orc_id = models.CharField(max_length=40)
    interests = models.TextField()

    def __str__(self):
        return self.full_name

# Create your models here.