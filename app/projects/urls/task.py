from django.urls import path
from projects.views.task import TaskDetail
from projects.views.comment import CommentList

urlpatterns = [
    path("/<int:id>", TaskDetail.as_view(), name="task-detail"),
    path("/<int:task_id>/comments", CommentList.as_view(), name="task-comments"),
]
