# from django.shortcuts import render,redirect

# from database.models import User, UserHistory, WorkPlan
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout

# from django.contrib import messages

# from datetime import datetime

# def index(request):
#     today = datetime.now()
#     user = User.objects.get(username=request.user.username)
#     data = UserHistory.objects.filter(user=user).filter(
#         plan__datetime_start__month = datetime.now().month,
#         plan__datetime_start__day = datetime.now().day,
#         plan__datetime_start__year = datetime.now().year)
#     return render(request, 'employee/index.html',{
#         'data':data,
#         'today':today,
#         })

# def info(request):
#     return render(request, 'employee/info.html',)

# def historyInfo(request,id):
#     data = UserHistory.objects.get(id=id)
#     thisdate = data.plan.datetime_start.date
#     return render(request, 'employee/historyInfo.html',{
#         'data':data,
#         'thisdate':thisdate,
#     })

# def planInfo(request,id):
#     data = UserHistory.objects.get(id=id)
#     thisdate = data.plan.datetime_start.date
#     return render(request, 'employee/planInfo.html',{
#         'data':data,
#         'thisdate':thisdate,
#     })
    
# def plan(request):
#     user = User.objects.get(username=request.user.username)
#     data = []
#     thismonth = str(datetime.now().year)+'-'+str(datetime.now().month)
#     time=""
#     if request.method == 'POST' and request.POST['month']:
#         time=request.POST['month']
#         year = request.POST['month'][0:4]
#         month = request.POST['month'][5:]
#         data = UserHistory.objects.filter(
#             user=user,
#             plan__datetime_start__month=month,
#             plan__datetime_start__year=year,
#             ).filter(
#                 plan__datetime_start__day__gt=datetime.now().day
#                 ).order_by(
#                     '-datetime_checkin'
#                     )
#     return render(request, 'employee/plan.html',{
#         'data':data,
#         'thismonth':thismonth,
#         'time':time
#         })

# def history(request):
#     user = User.objects.get(username=request.user.username)
#     data = []
#     thismonth = str(datetime.now().year)+'-'+str(datetime.now().month)
#     time=''
#     if request.method == 'POST' and request.POST['month']:
#         time = request.POST['month']
#         year = request.POST['month'][0:4]
#         month = request.POST['month'][5:]
#         data = UserHistory.objects.filter(
#             user=user,
#             plan__datetime_start__month=month,
#             plan__datetime_start__year=year).filter(
#                 plan__datetime_end__lt=datetime.now()).order_by('plan__datetime_start')
#     print(data)
#     return render(request,'employee/history.html',{
#         'data':data,
#         'time':time,
#         'thismonth':thismonth
#         })