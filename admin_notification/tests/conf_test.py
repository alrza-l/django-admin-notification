from django.test import TestCase
from django.apps import apps as django_apps
from django.conf import settings
from admin_notification.conf import custom_settings


class TestRetrieveModelsFromSettings(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.notification_models = settings.NOTIFICATION_MODELS

    def test_retrieve_model_names(self):
        self.assertEqual(
            self.notification_models,
            custom_settings.notification_models,
            f"{custom_settings.__module__}: custom_settings.notification_mdoels is not correct",
        )

    def test_evaluat_models(self):
        for model in self.notification_models:
            model_e = django_apps.get_model(model)
            self.assertEqual(model_e, custom_settings.get_selected_model(model))
