from django.contrib import admin


from projects.models import Project, ProjectMember, Task, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )


admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
    )


admin.site.register(ProjectMember, ProjectMemberAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "priority",
        "status",
    )


admin.site.register(Task, TaskAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "created_at",
    )


admin.site.register(Comment, CommentAdmin)
