from datetime import datetime
from django.shortcuts import redirect, render
from adm.forms import AddManagerForm, WorkGroupPlan,UserForm
from database.models import User, UserHistory, WorkGroup
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# ---------------------------------------- กลุ่มงาน -----------
def index(request):
    if 'addworkgroup' in request.POST:
        return redirect('adm:addWorkGroup')
    data = WorkGroup.objects.all()
    return render(request, 'adm/index.html',{
        'data':data})

def info(request):
    if request.method == "POST":
        if 'changepassword' in request.POST:
            return redirect('adm:selfChangePass')
    return render(request, 'adm/info.html')

def addWorkGroup(request):
    form = WorkGroupPlan()
    if request.method == "POST":
        form = WorkGroupPlan(request.POST)  
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('/')
    return render(request, 'adm/addWorkGroup.html' ,{
        'form':form
    })

def group(request,gid):
    if 'addmanager' in request.POST:
        return redirect('adm:addGroupManager',gid=gid)
    group = WorkGroup.objects.get(id=gid)
    data = WorkGroup.objects.get(id=gid).manager.all
    return render(request, 'adm/group.html',{
        'group':group,
        'data':data,
    })

def addGroupManager(request,gid):
    group = WorkGroup.objects.get(id=gid)
    data = group.manager.all()
    manager = []
    # user = User.objects.filter(roles="หัวหน้างาน")
    for user in User.objects.filter(roles="หัวหน้างาน"):
        if user not in data:
            manager.append(user)
    if request.method == "POST":
        if 'addmanager' in request.POST:
            for user_id in request.POST.getlist('เพิ่มหัวหน้างาน'):
                user = User.objects.get(id=user_id)
                group.manager.add(user)
        return redirect('adm:group',gid=gid)
    return render(request, 'adm/addGroupManager.html',{
        'group':group,
        'data':data,
        'manager':manager
    })

def deleteManager(request,gid,mid):
    user = User.objects.get(id=mid)
    WorkGroup.objects.get(id=gid).manager.remove(user)
    return redirect('adm:group',gid=gid)

def deleteWorkGroup(request,gid):
    WorkGroup.objects.get(id=gid).delete()
    return redirect('/')

# ---------------------------------------- ผู้ใช้งาน -----------
def userInfo(request):
    data = User.objects.all().exclude(roles="ผู้ดูแล")
    if 'register' in request.POST:
        return redirect('adm:register')
    return render(request,'adm/userInfo.html',{
        'data':data
    })
    
def register(request):
    form = UserForm()
    if request.method== 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm:userInfo')
        else:
            print("invalid")
    return render(request,'adm/register.html',{'form':form})

def deleteUser(request,uid):
    User.objects.get(id=uid).delete()
    return redirect('adm:userInfo')

def eachUser(request,uid):
    if request.method == "POST":
        if 'edit' in request.POST:
            user = User.objects.get(id=uid)
            if user.roles=="หัวหน้างาน" and request.POST.get('roles') != "หัวหน้างาน":
                work = WorkGroup.objects.filter(manager=user)
                print('demote')

            elif user.roles=="พนักงาน" and request.POST.get('roles') != "พนักงาน":
                print('promote')
                work = UserHistory.objects.filter(
                    user=user,
                    plan__datetime_start__gt=datetime.now()).delete()
            user.username=request.POST.get('username')
            user.first_name=request.POST.get('first_name')
            # print(user)
            user.last_name=request.POST.get('last_name')
            user.email=request.POST.get('email')
            user.roles=request.POST.get('roles')
            user.save()
        elif 'changepassword' in request.POST:
            return redirect('adm:changepassword',uid=uid)
        elif 'delete' in request.POST:
            return redirect('adm:deleteUser',uid=uid)
        return redirect('adm:userInfo')
    data = User.objects.get(id=uid)
    return render(request,'adm/eachUser.html',{
        'data':data
    })

def changepassword(request,uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
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
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('adm:userInfo')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'adm/changepassword.html', {
        'form': form
    })
