from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from adm.forms import WorkGroupPlan,UserForm
from database.models import Branchs, ManageBranchs, UserHistories, Users, WorkBranchs, WorkGroups
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# ---------------------------------------- กลุ่มงาน -----------
def index(request):
    # if 'addBranch' in request.POST:
        # pass
        # return redirect('adm:addWorkGroup')
    data = Branchs.objects.all()
    return render(request, 'adm/index.html',{
        'data':data})

def info(request):
    if request.method == "POST":
        if 'changepassword' in request.POST:
            return redirect('adm:selfChangePass')
    return render(request, 'adm/info.html')

def branch(request,name):
    branch = Branchs.objects.get(name=name)
    manager = ManageBranchs.objects.filter(branch=branch).first()
    if manager is not None:
        manager = Users.objects.get(id=manager.manager.id)
    else:
        manager = []
    group = WorkGroups.objects.filter(branch=branch)
    worker = WorkBranchs.objects.filter(branch=branch)
    if request.method == "POST":
        if 'addmanager' in request.POST:
            return redirect('adm:addmanager',name=name)
        elif 'addgroup' in request.POST:
            return redirect('adm:addGroup',name=name)
        elif 'addworker' in request.POST:
            return redirect('adm:addworker',name=name)
    return render(request, 'adm/branch.html',{
        'branch':branch,
        'manager':manager,
        'group':group,
        'worker':worker,
    })

def addmanager(request,name):
    branch = Branchs.objects.get(name=name)
    all_manager = ManageBranchs.objects.all()
    busy_manager = []
    for manager in all_manager:
        busy_manager.append(manager.manager)
    free_manager = []
    for manager in Users.objects.filter(roles="หัวหน้างาน"):
        if manager not in busy_manager:
            free_manager.append(manager)
    if request.method=="POST":
        print('post')
        if 'addmanager' in request.POST:
            for user_id in request.POST.getlist('เพิ่มหัวหน้างาน'):
                ManageBranchs.objects.create(
                    branch=branch,
                    manager=Users.objects.get(id=user_id))
        return redirect('adm:branch',name=name)
    return render(request, 'adm/addManager.html',{
        'free_manager':free_manager,
        'branch':branch
    })

def removeManager(request,name,mid):
    ManageBranchs.objects.get(
        branch__name=name,
        manager__id=mid).delete()
    return redirect('adm:branch',name=name)

def addGroup(request,name):
    branch = Branchs.objects.get(name=name)
    if request.method == "POST":
        if ('submit' in request.POST) and request.POST['group_name']:
            WorkGroups.objects.create(
                branch=branch,
                group_name=request.POST['group_name']
            )
        return redirect('adm:branch',name=name)
    return render(request,'adm/addGroup.html',{
        'branch':branch,
    })

def deleteGroup(request,name,gid):
    branch = Branchs.objects.get(name=name)
    WorkGroups.objects.get(id=gid).delete()
    return redirect('adm:branch',name=name)

def addworker(request,name):
    branch = Branchs.objects.get(name=name)
    all_worker = WorkBranchs.objects.all()
    busy_worker = []
    for worker in all_worker:
        busy_worker.append(worker.user)
    free_worker = []
    for worker in Users.objects.filter(roles="พนักงาน"):
        if worker not in busy_worker:
            free_worker.append(worker)
    if request.method=="POST":
        print('post')
        if 'addWorker' in request.POST:
            for user_id in request.POST.getlist('เพิ่มพนักงาน'):
                WorkBranchs.objects.create(
                    branch=branch,
                    user=Users.objects.get(id=user_id))
        return redirect('adm:branch',name=name)
    return render(request, 'adm/addWorker.html',{
        'free_worker':free_worker,
        'branch':branch
    })
def removeWorker(request,name,uid):
    branch = Branchs.objects.get(name=name)
    WorkBranchs.objects.get(
        branch=branch,
        user=Users.objects.get(id=uid)
        ).delete()
    return redirect('adm:branch',name=name)

# ---------------------------------------- ผู้ใช้งาน -----------
def allUser(request):
    data = Users.objects.all().exclude(roles="ผู้ดูแล")
    all_manager = Users.objects.filter(roles="หัวหน้างาน").count()
    all_worker = Users.objects.filter(roles="พนักงาน").count()
    all_admin = Users.objects.filter(roles="ผู้ดูแล").count()
    all = int(all_manager)+int(all_worker)+int(all_admin)
    if 'register' in request.POST:
        return redirect('adm:register')
    return render(request,'adm/allUser.html',{
        'data':data,
        'all_manager':all_manager,
        'all_worker':all_worker,
        'all_admin':all_admin,
        'all':all,

    })
    
def register(request):
    form = UserForm()
    if request.method== 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm:allUser')
    return render(request,'adm/register.html',{'form':form})

def deleteUser(request,uid):
    Users.objects.get(id=uid).delete()
    return redirect('adm:allUser')

def userInfo(request,uid):
    if request.method == "POST":
        if 'edit' in request.POST:
            user = Users.objects.get(id=uid)
            if user.roles=="หัวหน้างาน" and request.POST.get('roles') != "หัวหน้างาน":
                pass
                # work = WorkGroups.objects.filter(manager=user).delete()
            elif user.roles=="พนักงาน" and request.POST.get('roles') != "พนักงาน":
                pass
                # work = UserHistories.objects.filter(
                #     user=user,
                #     plan__datetime_start__gt=datetime.now()).delete()
            user.username=request.POST.get('username')
            user.first_name=request.POST.get('first_name')
            user.last_name=request.POST.get('last_name')
            user.email=request.POST.get('email')
            user.roles=request.POST.get('roles')
            user.save()
        elif 'changepassword' in request.POST:
            return redirect('adm:changepassword',uid=uid)
        elif 'delete' in request.POST:
            return redirect('adm:deleteUser',uid=uid)
        return redirect('adm:allUser')
    data = Users.objects.get(id=uid)
    return render(request,'adm/userInfo.html',{
        'data':data
    })

def changepassword(request,uid):
    user = Users.objects.get(id=uid)
    if request.method == 'POST':
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('adm:eachUser',uid=uid)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(user=user)
    return render(request, 'adm/changepassword.html', {
        'form': form
    })

def selfChangePass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('adm:userInfo')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'adm/changepassword.html', {
        'form': form
    })
