from django.contrib import admin
from .models import Task, Comment, Tag
# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Tag)