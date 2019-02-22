from django.db import models
from django.utils.translation import get_language, gettext_lazy as _


# Create your models here.

class Contact(models.Model):
    OTHER = 0
    PHONE_NUMBER = 1
    EMAIL = 2
    SOCIAL_NET = 3
    POST_INDEX = 4

    INDEX = (
        (OTHER, "other"),
        (PHONE_NUMBER, "phone number"),
        (EMAIL, "email"),
        (SOCIAL_NET, "social network"),
        (POST_INDEX, "post index")
    )

    name = models.CharField(max_length=255, blank=False)
    selection_committee = models.BooleanField(default=False)
    index = models.IntegerField(choices=INDEX, default=OTHER)

    def __str__(self):

        return str(self.name) + ("\tselection_committee" if self.selection_committee else " ")
