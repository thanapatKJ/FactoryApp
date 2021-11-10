from django.shortcuts import render,redirect

from database.models import User, UserHistory, WorkPlan
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib import messages

from datetime import datetime

def index(request):
    today = datetime.now()
    user = User.objects.get(username=request.user.username)
    data = UserHistory.objects.filter(user=user).filter(
        plan__datetime_start__month = datetime.now().month,
        plan__datetime_start__day = datetime.now().day,
        plan__datetime_start__year = datetime.now().year)

    return render(request, 'employee/index.html',{
        'data':data,
        'today':today,
        })

def info(request):
    return render(request, 'employee/info.html',)


def plan(request):
    user = User.objects.get(username=request.user.username)
    data = UserHistory.objects.filter(user=user).filter(plan__datetime_start__gte=datetime.now()).order_by('-datetime_checkin')

    print(data)
    # if request.method == 'POST':
    #     year = request.POST['month'][0:4]
    #     month = request.POST['month'][5:]
    return render(request, 'employee/plan.html',{'data':data})

def history(request):
    user = User.objects.get(username=request.user.username)
    data = UserHistory.objects.filter(user=user).filter(plan__datetime_end__lt=datetime.now()).order_by('datetime_checkin')
    return render(request,'employee/history.html',{'data':data})