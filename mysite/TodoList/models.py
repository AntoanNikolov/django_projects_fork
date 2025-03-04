from django.db import models

# Create your models here.
class Task(models.Model):
    task_summary =  models.CharField(max_length=200)
    task_details = models.CharField(max_length=200)
    def __str__(self):
        return self.task_summary
    
class Comment(models.Model) :
    text = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
