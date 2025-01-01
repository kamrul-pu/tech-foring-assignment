from rest_framework import serializers

from projects.models import Project, ProjectMember
from core.serializers.user import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "owner",
            "created_at",
        )


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = (
            "id",
            "project",
            "user",
            "role",
        )
