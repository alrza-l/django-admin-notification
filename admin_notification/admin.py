from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Notification

admin.site.register(Notification)
admin.site.register(LogEntry)
