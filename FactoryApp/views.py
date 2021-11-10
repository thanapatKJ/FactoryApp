from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import UserForm

from django.contrib import messages

@login_required
def index(request):
    if request.user.roles == 'ผู้ดูแล':
        return redirect('/admin/')
    elif request.user.roles == 'หัวหน้างาน':
        return redirect('/manager/')
    elif request.user.roles == 'พนักงาน':
        return redirect('/employee/')
    else:
        return redirect('/logout/')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        user = authenticate(request ,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username หรือ Password ไม่ถูกต้อง')
    return render(request,'login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method== 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print("invalid")
        else:
            form = UserForm()
    form = UserForm(request.POST)
    return render(request,'register.html',{'form':form})
