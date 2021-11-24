from django.urls import path
from . import views

app_name = "adm"

urlpatterns = [
    # กลุ่มงาน
    path('',views.index, name="index"),
    path('info/',views.info, name="info"),
    path('info/selfChangePass/',views.selfChangePass, name="selfChangePass"),
    path('branch/<str:name>/',views.branch, name="branch"),
    path('branch/<str:name>/addmanager/',views.addmanager, name="addmanager"),
    path('branch/<str:name>/removeManager/<str:mid>',views.removeManager, name="removeManager"),
    path('branch/<str:name>/addGroup/',views.addGroup, name="addGroup"),
    path('branch/<str:name>/deleteGroup/<str:gid>',views.deleteGroup, name="deleteGroup"),
    path('branch/<str:name>/addworker/',views.addworker, name="addworker"),
    path('branch/<str:name>/removeWorker/<str:uid>',views.removeWorker, name="removeWorker"),
    path('branch-new/',views.addBranch, name="addBranch"),
    path('branch/<str:name>/deleteBranch',views.deleteBranch, name="deleteBranch"),

    # ผู้ใช้งาน
    path('user/',views.allUser, name="allUser"),
    path('user/<str:uid>/',views.userInfo, name="userInfo"),
    path('user/<str:uid>/delete/',views.deleteUser, name="deleteUser"),
    path('user/<str:uid>/changepassword/',views.changepassword, name="changepassword"),
    path('user/register/new/',views.register, name="register"),


]
