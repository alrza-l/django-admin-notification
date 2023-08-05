from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Notification(models.Model):
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model.name} notifications"
