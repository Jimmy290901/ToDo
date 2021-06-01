from django.contrib import admin

# Register your models here.
from .models import MyTasks

admin.site.register(MyTasks)