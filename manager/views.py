from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime
from database.models import Branchs, ManageBranchs, UserHistories, WorkBranchs, WorkGroups, WorkPlans, Users
import json
from .forms import WorkPlanForm


# ------------------------------------------------------------------------------------------------------------
# กลุ่มงาน
def index(request):
    today = datetime.now()
    branch = ManageBranchs.objects.filter(manager=request.user).first().branch
    all_groups = WorkGroups.objects.filter(branch=branch)
    today_groups = []
    for group in all_groups:
        for plan in WorkPlans.objects.filter(group_name=group,datetime_start__year=today.year,
                    datetime_start__month=today.month,
                    datetime_start__day=today.day):
            worker = UserHistories.objects.filter(plan=plan).count()
            workerIn = UserHistories.objects.filter(plan=plan).exclude(datetime_checkin__isnull=True).count()
            today_groups.append({'plan':plan,'worker':worker,'workerIn':workerIn})
    return render(request,'manager/index.html',{
        'today':today,
        'data':today_groups,
    })

def group(request,gid):
    return render(request,'manager/groupChoice.html')
#---------------------------------------------------------------
# แผนงาน
def Allplan(request):
    date = datetime.today().strftime('%Y-%m-%d')
    branch = ManageBranchs.objects.filter(manager=request.user).first().branch
    all_group = WorkGroups.objects.filter(branch=branch)
    selected_group = []
    if request.method == "POST":
        if 'addPlan' in request.POST:
            return redirect('manager:addPlan')
        else:
            date = request.POST['date']
            year = request.POST['date'][0:4]
            month = request.POST['date'][5:7]
            day = request.POST['date'][8:]
            choose_group = request.POST.getlist('เลือกกลุ่มงาน')
            for group in choose_group:
                group_id = WorkGroups.objects.filter(group_name=group).first().id
                plan = WorkPlans.objects.filter(group_name=group_id,datetime_start__day=day,datetime_start__month=month,datetime_start__year=year).first()
                if plan:
                    selected_group.append({
                        "group_name":group,
                        "worker":UserHistories.objects.filter(plan=plan).count(),
                        "group":plan
                    })
    else:
        for group in all_group:
            plan = WorkPlans.objects.filter(group_name=group,datetime_start__day=datetime.now().day,datetime_start__month=datetime.now().month,datetime_start__year=datetime.now().year).first()
            if plan:
                worker =UserHistories.objects.filter(plan=plan)
                selected_group.append({
                    "group_name":group.group_name,
                    "worker":worker.count(),
                    "group":plan
                })
    return render(request,'manager/allPlan.html',{
        'date':date,
        'all_group':all_group,
        'data':selected_group
    })

def addPlan(request):
    branch = ManageBranchs.objects.filter(manager=request.user).first()
    all_group = WorkGroups.objects.filter(branch=branch.branch)
    if request.method == "POST":
        if 'ยืนยันเพิ่มงาน' in request.POST:
            datetime_start = request.POST['datetime_start'][0:10]+" "+request.POST['datetime_start'][11:16]
            datetime_end = request.POST['datetime_end'][0:10]+" "+request.POST['datetime_end'][11:16]
            limit_ot = request.POST['limit_ot']
            group = WorkGroups.objects.get(group_name=request.POST['เลือกกลุ่มงาน'])
            WorkPlans.objects.create(
                group_name=group,
                datetime_start=datetime_start,
                datetime_end=datetime_end,
                limit_ot_hour=limit_ot)
            return redirect('manager:Allplan')
    return render(request,'manager/addPlan.html',{
        'all_group':all_group
    })

def deletePlan(request,pid):
    WorkPlans.objects.get(id=pid).delete()
    return redirect('manager:Allplan')

def plan(request,pid):
    plan = WorkPlans.objects.get(id=pid)
    list_worker = UserHistories.objects.filter(plan=plan)
    if 'addUser' in request.POST:
        return redirect('manager:addUser',pid=pid)
    return render(request,'manager/plan.html',{
        'plan':plan,
        'list_worker':list_worker,
    })

def removeUser(request,pid,uid):
    UserHistories.objects.get(
        user=uid,
        plan=pid).delete()
    return redirect('manager:plan',pid=pid)

def addUser(request,pid):
    plan = WorkPlans.objects.get(id=pid)
    if request.method=="POST":
        if 'ยืนยันเพิ่มพนักงาน' in request.POST:
            for user in request.POST.getlist('เลือกกลุ่มงาน'):
                thisUser = Users.objects.get(id=user)
                UserHistories.objects.create(
                    user=thisUser,
                    plan=plan)
            return redirect('manager:plan',pid=pid)
    else:
        branch = ManageBranchs.objects.get(manager=request.user).branch
        busy_user = UserHistories.objects.filter(plan__group_name__branch=branch)
        busy_userID = []
        for user in busy_user:
            busy_userID.append(user.user)
        worker_branch = WorkBranchs.objects.filter(branch=branch)
        worker_branchID = []
        for worker in worker_branch:
            worker_branchID.append(worker.user)
        list_worker=set(worker_branchID).difference(set(busy_userID))
    return render(request,'manager/addUser.html',{
        'plan':plan,
        'list_worker':list_worker,
    })

#---------------------------------------------------------------
# ข้อมูลพนักงาน
def info(request):
    branch = ManageBranchs.objects.filter(manager=request.user).first()
    return render(request,'manager/info.html',{
        'branch':branch
    })

#---------------------------------------------------------------
# เพิ่มกลุ่ม
def add(request):
    branch = ManageBranchs.objects.filter(manager=request.user).first().branch
    if 'submit' in request.POST:
        WorkGroups.objects.create(branch=branch,group_name=request.POST['group_name'])
        return redirect('manager:allGroup')
    elif 'cancel' in request.POST:
        return redirect('manager:allGroup')
    return render(request,'manager/add.html',{
        'branch':branch
    })

def allGroup(request):
    branch = ManageBranchs.objects.filter(manager=request.user).first().branch
    data = WorkGroups.objects.filter(branch=branch)
    if 'addPlan' in request.POST:
        return redirect('manager:add')
    return render(request,'manager/allGroup.html',{
        'branch':branch,
        'data':data
    })

def deleteGroup(request,gid):
    WorkGroups.objects.get(id=gid).delete()
    return redirect('manager:allGroup')