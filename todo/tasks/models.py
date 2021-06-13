from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class MyTasks(models.Model):
    title = models.CharField(max_length=500)
    createdDate = models.DateTimeField(default=timezone.now)
    isComplete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("updateTask", kwargs={"task_id": self.id})