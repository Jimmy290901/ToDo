from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['registerDate']
        # fields = ("__all__")
        widgets = {
            'password': forms.PasswordInput(),
        #     'name': forms.TextInput(attrs={'placeholder':'Name'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),

        #     # 'registerDate': forms.DateTimeField(required=False),
        }