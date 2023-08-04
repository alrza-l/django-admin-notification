from __future__ import unicode_literals
from django.contrib.auth.models import User
from admin_notification.cache import del_cached_active_item
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from six import python_2_unicode_compatible
from django.contrib.contenttypes.models import ContentType


@python_2_unicode_compatible
class Notification(models.Model):
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model.name} notifications"
