from django import forms
from .models import MyTasks
from django.urls import reverse

class MyTaskForm(forms.ModelForm):
    
    class Meta:
        model = MyTasks
        exclude = ['createdDate', 'isComplete']

    # def __init__(self, user_id):
    #     self.user_id = user_id