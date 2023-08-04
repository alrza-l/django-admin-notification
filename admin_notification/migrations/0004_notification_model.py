# Generated by Django 4.1.9 on 2023-08-04 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("admin_notification", "0003_alter_notification_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="model",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
            preserve_default=False,
        ),
    ]