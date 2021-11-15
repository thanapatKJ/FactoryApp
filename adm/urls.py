from django.urls import path
from . import views

app_name = "adm"

urlpatterns = [
    # กลุ่มงาน
    path('',views.index, name="index"),
    path('info/',views.info, name="info"),
    path('info/selfChangePass/',views.selfChangePass, name="selfChangePass"),
    path('addWork/',views.addWorkGroup, name="addWorkGroup"),
    path('group/<str:gid>/deleteWorkGroup/',views.deleteWorkGroup, name="deleteWorkGroup"),
    path('group/<str:gid>/',views.group, name="group"),
    path('group/<str:gid>/add/',views.addGroupManager, name="addGroupManager"),
    path('group/<str:gid>/deleteManager/<str:mid>/',views.deleteManager, name="deleteManager"),
    # ผู้ใช้งาน
    path('user/',views.userInfo, name="userInfo"),
    path('user/<str:uid>/delete/',views.deleteUser, name="deleteUser"),
    path('user/<str:uid>/',views.eachUser, name="eachUser"),
    path('user/<str:uid>/changepassword/',views.changepassword, name="changepassword"),
    path('user/register/new/',views.register, name="register"),


]
