from django.apps import apps as django_apps
from django.conf import LazySettings
from django.core.exceptions import ImproperlyConfigured


class Settings(LazySettings):
    def get_selected_model(self, model_name: str):
        model = django_apps.get_model(model_name)
        return model

    @property
    def notification_models(self):
        try:
            models = self.NOTIFICATION_MODELS
        except AttributeError:
            raise ImproperlyConfigured(
                "The 'NOTIFICATION_MODELS' setting is missing in settings.py. Make sure to define 'NOTIFICATION_MODELS' with the correct value."
            )
        return models


custom_settings = Settings()
