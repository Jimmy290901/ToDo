from django.db import models
from django.utils import timezone
from django.urls import reverse
from passlib.hash import pbkdf2_sha256
# Create your models here.

#To Do
class User(models.Model):
    user_id = models.AutoField(primary_key=True) #no fill-up required
    name = models.CharField(max_length=500)
    registerDate = models.DateTimeField(default=timezone.now) #no fill-up required
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("tasks", kwargs={"user_id": self.user_id})
    
    def verify_password(self, givenPassword):
        return pbkdf2_sha256.verify(givenPassword, self.password)
    