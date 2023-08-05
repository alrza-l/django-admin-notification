from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from admin_notification.conf import custom_settings
from admin_notification.models import Notification


@receiver(post_save)
def post_save_handler(sender, **kwargs):
    models = custom_settings.notification_models
    sender_label = str(sender._meta.label)
    if kwargs["created"] and sender_label in models:
        app_label, model_name = sender_label.split(".")
        model_ct = ContentType.objects.get(app_label=app_label, model=model_name)
        notification, _ = Notification.objects.get_or_create(model=model_ct)
        notification.count += 1
        notification.save()
