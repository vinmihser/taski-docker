"""Параметры для сериализатора."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Базовое описание класса."""

    class Meta:
        """Описание Метакласса."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
