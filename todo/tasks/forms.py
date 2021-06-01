from django import forms
from .models import MyTasks

class MyTaskForm(forms.ModelForm):
    
    class Meta:
        model = MyTasks
        fields = ("__all__")
