from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from admin_notification.enums import ActionsEnum


def validate_notification_models():
    if isinstance(list, settings.NOTIFICATION_MODELS):
        return {model: [list(ActionsEnum)] for model in settings.NOTIFICATION_MODELS}
    elif isinstance(dict, settings.NOTIFICATION_MODELS):
        return settings.NOTIFICATION_MODELS
    else:
        raise ImproperlyConfigured(
            "NOTIFICATION_MODELS must be of the form 'app_label.model_name' or a dictionary of models with actions in a list"
        )


NOTIFICATION_MODELS = validate_notification_models()
