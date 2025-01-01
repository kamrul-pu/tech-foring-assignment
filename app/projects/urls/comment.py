from django.urls import path

from projects.views.comment import CommentList, CommentDetail


urlpatterns = [
    path("/<int:id>", CommentDetail.as_view(), name="comment-detail"),
]
