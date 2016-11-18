from django.contrib import admin
from blog.models import Post, Comment, Task, TaskNote, WebLink, Project, Department, Contact, ContactNote

# Register your models here.
admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Task)

admin.site.register(TaskNote)

admin.site.register(WebLink)

admin.site.register(Department)

admin.site.register(Project)

admin.site.register(Contact)

admin.site.register(ContactNote)