from django.urls import path, include


urlpatterns = [
    path("/projects", include("projects.urls.project"), name="project-urls"),
    path("/tasks", include("projects.urls.task"), name="task-urls"),
    path("/comments", include("projects.urls.comment"), name="comment-urls"),
]
