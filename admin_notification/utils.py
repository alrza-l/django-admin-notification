from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class Settings:
    def __init__(self):
        self.NOTIFICATION_MODELS = self.get_notification_models()

    @staticmethod
    def get_selected_model(self, model_name: str):
        model = django_apps.get_model(model_name)
        return model

    @property
    def get_notification_models(self):
        try:
            models = settings.NOTIFICATION_MODELS
        except ValueError:
            raise ImproperlyConfigured(
                "NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
            )
        return models
