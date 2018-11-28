from django.db import models


class Footer(models.Model):
    location = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20)
    site = models.CharField(max_length=100)







