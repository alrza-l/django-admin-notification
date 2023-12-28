from django.db.models import TextChoices


class ActionChoices(TextChoices):
    CREATE = "create", "Create"
    DELETE = "delete", "Delete"
    UPDATE = "update", "Update"
