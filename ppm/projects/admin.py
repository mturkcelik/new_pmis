from django.contrib import admin
from .models import Project, Post, Like, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'assigned_to')


admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
