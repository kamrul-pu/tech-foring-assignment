from rest_framework import serializers

from projects.models import Task
from core.serializers.user import UserSerializer
from projects.serializers.project import ProjectSerializer


class TaskSerializer(serializers.ModelSerializer):
    # assigned_to = UserSerializer(read_only=True)
    # project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "priority",
            "assigned_to",
            "project",
            "created_at",
            "due_date",
        )
