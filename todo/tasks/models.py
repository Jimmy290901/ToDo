from django.db import models
from django.urls import reverse
# Create your models here.

class MyTasks(models.Model):
    title = models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True)
    isComplete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("updateTask", kwargs={"task_id": self.id})