from django.contrib.auth import get_user_model

from django.db import models

from projects.choices import MemberRole, TaskStatus, TaskPriority


User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_projects"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_members", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10, choices=MemberRole.choices, default=MemberRole.MEMBER
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Task(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=TaskStatus.choices, default=TaskStatus.IN_PROGRESS
    )
    priority = models.CharField(
        max_length=10, choices=TaskPriority.choices, default=TaskPriority.LOW
    )
    assigned_to = models.ForeignKey(
        User,
        related_name="user_tasks",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
