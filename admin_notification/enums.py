from django.db.models import TextChoices


class ActionsEnum(TextChoices):
    CREATE = "create", "Create"
    DELETE = "delete", "Delete"
    UPDATE = "update", "Update"
