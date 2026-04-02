"""Модели данных для API приложения."""

from django.db import models


class Task(models.Model):
    """Описание поля Task с дополнительной информацией."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        """Возвращает собственный заголовок title."""
        return self.title
