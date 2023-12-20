from django.apps import apps as django_apps
from django.apps.registry import Apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import HttpResponse, redirect, render

from admin_notification.models import Notification


def post_save_handler(sender, instance, **kwargs):
    if kwargs["created"]:
        print("called1")
        model_ct = ContentType.objects.get_for_model(sender)
        notification, _ = Notification.objects.get_or_create(model=model_ct)
        notification.count += 1
        notification.save()
        notification.update_to_cache()


try:
    for model in settings.NOTIFICATION_MODELS:
        model = django_apps.get_model(model, require_ready=False)
        post_save.connect(post_save_handler, model)
except ValueError:
    raise ImproperlyConfigured(
        "NOTIFICATION_MODELS must be of the form 'app_label.model_name'"
    )
