"""Настройки админской части."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Профиль пользователя admin с дополнительной информацией."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
