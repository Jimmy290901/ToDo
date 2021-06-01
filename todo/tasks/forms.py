from django import forms
from .models import MyTasks
from django.urls import reverse

class MyTaskForm(forms.ModelForm):
    
    class Meta:
        model = MyTasks
        fields = ("__all__")
    
