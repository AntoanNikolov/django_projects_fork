from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Task(models.Model):
    task_summary =  models.CharField(max_length=200)
    task_details = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag') #task can have many tags that belong to it, a tag can belong to many tasks
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.task_summary
    
class Comment(models.Model) :
    text = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #we are using updated_at with auto_now since we are not updating comments, therefore, we can use them interchangeably with created_at and auto_now_add
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.text

class Tag(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text