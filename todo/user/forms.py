from django import forms
from .models import User

class UserSignUpForm(forms.ModelForm):
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

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['name', 'registerDate']
        widgets = {
            'email' : forms.EmailInput(attrs={'placeholder':'Email'}),
            'password' : forms.PasswordInput(attrs={'placeholder':'Password'}),
        }
