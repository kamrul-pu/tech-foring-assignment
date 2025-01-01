from django.urls import path

from projects.views.project import ProjectList, ProjectDetail
from projects.views.task import TaskList

urlpatterns = [
    path("", ProjectList.as_view(), name="project-list"),
    path("/<int:id>", ProjectDetail.as_view(), name="project-detail"),
    path("/<int:project_id>/tasks", TaskList.as_view(), name="project-tasks"),
]
