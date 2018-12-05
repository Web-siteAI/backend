from django.db import models
# Create your models hereще


class News(models.Model):
    topic = models.CharField(max_length=255)
    short_description = models.TextField(null=False)
    post = models.TextField(null=False)
    data_post = models.DateField(null=True)
    photo = models.ImageField(blank=True, upload_to="pictures/%Y/%m/%D/", null=True, max_length=255)

