from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from projects.models import Comment
from projects.serializers.comment import CommentSerializer


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get("task_id", None)
        queryset = Comment.objects.filter(task_id=task_id).order_by("-id")
        return queryset

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get("task_id", None)
        data = request.data.copy()
        data["task"] = task_id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    lookup_field = "id"
