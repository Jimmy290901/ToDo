from user.models import User
from user.forms import UserForm
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def login(request):
    if request.method == "POST":
        if 'signup' in request.POST:
            return redirect(signup)
    return render(request, 'user/login.html')

def signup(request):
    # print(request)
    signupForm = UserForm()
    err_msg = ''
    if request.method == 'POST':
        check = User.objects.filter(email=request.POST['email'])
        # print(check)
        signupForm = UserForm(request.POST)
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