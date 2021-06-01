from django.db import models

# Create your models here.

class MyTasks(models.Model):
    title = models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True)
    isComplete = models.BooleanField(default=False)