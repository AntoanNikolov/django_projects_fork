from django.db import models

# Create your models here.
class Task(models.Model):
    task_summary =  models.CharField(max_length=200)
    task_details = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.task_summary
    
class Comment(models.Model) :
    text = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    #we are using updated_at with auto_now since we are not updating comments, therefore, we can use them interchangeably with created_at and auto_now_add
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.text

class Tag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text