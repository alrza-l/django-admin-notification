from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import reverse

from admin_notification.models import Notification


def check_notification_view(request):
    id = request.GET.get("id")
    if id is not None:
        try:
            notification = Notification.objects.get(id=id)
            notification.count = 0
            notification.update_to_cache()
            notification.save()
            return redirect(notification.get_admin_link())
        except Notification.DoesNotExist:
            return reverse("admin:index")
    return reverse("admin:index")
