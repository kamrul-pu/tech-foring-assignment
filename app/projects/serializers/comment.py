from rest_framework import serializers

from core.serializers.user import UserSerializer

from projects.models import Comment
from projects.serializers.task import TaskSerializer


class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # task = TaskSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "user",
            "task",
            "created_at",
        )
