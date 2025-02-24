from django.db import models

# Create your models here.
class Service(models.Model):
    title =  models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class TimeSlot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    is_occupied = models.BooleanField()
    def __str__(self):
        return str(self.time)