from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from projects.models import Task

from projects.serializers.task import TaskSerializer


class TaskList(ListCreateAPIView):
    queryset = Task.objects.filter().order_by("-id")
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get("project_id", None)
        queryset = Task.objects.filter(project_id=project_id).order_by("-id")
        return queryset

    def post(self, request, *args, **kwargs):
        # Get the project_id from URL params
        project_id = kwargs.get("project_id", None)
        # Add the project_id to the request data so that it can be validated by the serializer
        data = request.data.copy()
        data["project"] = project_id
        # Initialize the serializer with the request data
        serializer = self.serializer_class(data=data)
        # Validate the data
        if serializer.is_valid(raise_exception=True):
            # Save the task if the data is valid
            task = serializer.save()
            # Return a response with the serialized data of the newly created task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    lookup_field = "id"
