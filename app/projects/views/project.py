from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from projects.models import Project

from projects.serializers.project import ProjectSerializer


class ProjectList(ListCreateAPIView):
    queryset = Project.objects.filter().order_by("-id")
    serializer_class = ProjectSerializer


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer
    lookup_field = "id"
