import random
from faker import Faker

from django.test import TestCase
from django.db import models
from django.contrib.contenttypes.models import ContentType

from admin_notification.models import Notification
from admin_notification.conf import custom_settings


class TestNotificationCreate(TestCase):
    def setUp(self) -> None:
        self.notification_model = Notification
        self.notification_models = [
            custom_settings.get_selected_model(x)
            for x in custom_settings.notification_models
        ]
        self.fake = Faker()

    def test_new_notification(self):
        for model in self.notification_models:
            fake_data = self.generate_fake_data(model)
            new_instance = model.objects.create(**fake_data)
            model_ct = ContentType.objects.get_for_model(new_instance)
            instance_noticifation = self.notification_model.objects.filter(
                model=model_ct
            )
            self.assertTrue(
                instance_noticifation.exists(),
                "Notification won't be created when a new model instance is created",
            )

    def test_duplicated_notifications(self):
        for model in self.notification_models:
            random_count = random.randint(1, 10)
            for count_ in range(random_count):
                fake_data = self.generate_fake_data(model)
                new_instance = model.objects.create(**fake_data)

            model_ct = ContentType.objects.get_for_model(new_instance)
            instance_notifications = self.notification_model.objects.filter(
                model=model_ct
            )
            self.assertEqual(
                instance_notifications.count(),
                1,
                "duplicated notifications are created",
            )

            notification_count = instance_notifications.aggregate(
                count=models.Sum("count")
            )["count"]

            self.assertEqual(
                notification_count,
                random_count,
                "There is a miscount in created models",
            )

    def generate_fake_data(self, model):
        data = dict()

        for field in model._meta.fields:
            if not field.auto_created:
                if isinstance(field, models.CharField):
                    field_data = self.fake.text(max_nb_chars=5)

                elif isinstance(field, models.IntegerField):
                    field_data = self.fake.random_int(1, 100)

                elif isinstance(field, models.BooleanField):
                    field_data = self.fake.boolean()

                elif isinstance(field, models.DateField):
                    field_data = self.fake.date()

                elif isinstance(field, models.ForeignKey):
                    related_model = field.related_model
                    related_objects = related_model.objects.all()
                    if related_objects.exists():
                        field_data = random.choice(related_objects)

                data.update({f"{field.name}": field_data})
        return data
