from django.forms.widgets import PasswordInput
from user.models import User
from user.forms import UserSignUpForm, UserLoginForm
from django.shortcuts import get_object_or_404, redirect, render
from passlib.hash import pbkdf2_sha256

# Create your views here.

def login(request):
    loginForm = UserLoginForm()
    err_msg = ''
    if request.method == "POST":
        print(request.POST['password'])
        check = User.objects.filter(email=request.POST['email'])
        loginForm = UserLoginForm(request.POST)
        if check.exists():
            user = User.objects.get(email=request.POST['email'])
            if user.verify_password(request.POST['password']):
                return redirect(user.get_absolute_url())
            else:
                err_msg = 'Password does not match!'
        else:
            err_msg = 'Email is not registered!'
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
                # print(newUser)'
                formName = request.POST['name']
                formEmail = request.POST['email']
                formPassword = pbkdf2_sha256.encrypt(request.POST['password'], rounds = 12000, salt_size=32)
                User.objects.create(name = formName, email = formEmail, password = formPassword)
                # signupForm.save()
                return redirect(login)
            else:
                err_msg = 'Enter a valid email ID!'
    context = {
        'signupForm': signupForm,
        'err_msg':err_msg,
    }
    return render(request, 'user/signup.html', context)