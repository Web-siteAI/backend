from django.db import models


# Create your models here.
class Cooperation(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return self.name
