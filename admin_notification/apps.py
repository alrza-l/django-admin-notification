from django.apps import AppConfig


class AdminNotificationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admin_notification"

    def ready(self):
        from admin_notification.models import Notification
        import admin_notification.signals
