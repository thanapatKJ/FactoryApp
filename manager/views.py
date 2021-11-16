from django.shortcuts import render
from datetime import datetime
from database.models import UserHistory, WorkGroup, WorkPlan

def index(request):
    today = datetime.now()
    data = WorkGroup.objects.filter(manager= request.user)
    todaywork = WorkPlan.objects.filter(
        datetime_start__day=datetime.now().day,
        datetime_start__month=datetime.now().month,
        datetime_start__year=datetime.now().year,
        )
    list_employee = UserHistory.objects.filter(
        plan__datetime_start__day=datetime.now().day,
        plan__datetime_start__month=datetime.now().month,
        plan__datetime_start__year=datetime.now().year,
    )
    # print(datetime.now().dat)
    print(todaywork)
    print(list_employee)
    return render(request,'manager/index.html',{
        'today':today,
        'data':data
    })

def Plan(request):
    thismonth = str(datetime.now().year)+'-'+str(datetime.now().month)
    selected_date = thismonth
    group = WorkGroup.objects.filter(manager = request.user)
    data=[]
    for object in group:
        group=[]
        for item in WorkPlan.objects.filter(work_group=object).filter(datetime_start__day__gt=datetime.now().day):
            group.append(item)
        
    print(data[0])
    if request.method == "POST":
        selected_date = request.POST['month']
        data = WorkPlan.objects.filter(
            work_group__work_group__manager__id = request.user.id)
    return render(request,'manager/Plan.html',{
        'selected_date':selected_date,
        'thismonth':thismonth,
        'data':data
    })