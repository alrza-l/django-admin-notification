from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AdminNotificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admin_notification"

    def ready(self):
        import admin_notification.signals
        from admin_notification.models import Notification
