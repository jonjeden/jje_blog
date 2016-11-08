from django.contrib import admin
from blog.models import Post, Comment, Task, TaskNote, WebLink

# Register your models here.
admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Task)

admin.site.register(TaskNote)

admin.site.register(WebLink)
