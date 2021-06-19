from django.forms.widgets import PasswordInput
from user.models import User
from user.forms import UserSignUpForm, UserLoginForm
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def login(request):
    loginForm = UserLoginForm()
    err_msg = ''
    if request.method == "POST":
        if 'signup' in request.POST:
            return redirect(signup)
        else:
            check = User.objects.filter(email=request.POST['email'], password = request.POST['password'])
            if check.exists():
                user = User.objects.get(email=request.POST['email'])
                return redirect(user.get_absolute_url())
            else:
                err_msg = 'Wrong Email or Password!'
    context = {
        'loginForm': loginForm,
        'err_msg': err_msg,
    }
    return render(request, 'user/login.html', context)

def signup(request):
    # print(request)
    signupForm = UserSignUpForm()
    err_msg = ''
    if request.method == 'POST':
        check = User.objects.filter(email=request.POST['email'])
        # print(check)
        signupForm = UserSignUpForm(request.POST)
        if check.exists():
            err_msg = 'Email Already Registered!'
        else:
            # print(request.POST)
            # print(newUser.is_valid())
            if signupForm.is_valid():
                # print(newUser)
                signupForm.save()
                return redirect(login)
            else:
                err_msg = 'Enter a valid email ID!'
    context = {
        'signupForm': signupForm,
        'err_msg':err_msg,
    }
    return render(request, 'user/signup.html', context)