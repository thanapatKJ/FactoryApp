from django.urls import path
from . import views

app_name='manager'
urlpatterns = [
    # กลุ่มงาน
    path('', views.index, name="index"),
    path('todayPlan/<str:pid>', views.todayPlan, name="todayPlan"),
    path('todayPlan/<str:pid>/removeWorker/<str:uid>', views.removeWorker, name="removeWorker"),
    path('todayPlan/<str:pid>/editOT/<str:uid>', views.editOT, name="editOT"),
    path('todayPlan/<str:pid>/addWorker/', views.addWorker, name="addWorker"),
    path('todayPlan/<str:pid>/checkin/', views.checkin, name="checkin"),
    path('todayPlan/<str:pid>/checkout/', views.checkout, name="checkout"),

    # แผนงาน
    path('plan/', views.Allplan, name="Allplan"),
    path('plan/<str:pid>/deletePlan', views.deletePlan, name="deletePlan"),
    path('plan/addPlan', views.addPlan, name="addPlan"),
    path('plan/<str:pid>/', views.plan, name="plan"),
    path('plan/<str:pid>/removeUser/<str:uid>', views.removeUser, name="removeUser"),
    path('plan/<str:pid>/addUser', views.addUser, name="addUser"),
    # ข้อมูล
    path('info/', views.info, name="info"),
    # เพิ่มกลุ่มงาน
    path('allGroup/', views.allGroup, name="allGroup"),
    path('add/', views.add, name="add"),
    path('deleteGroup/<str:gid>/', views.deleteGroup, name="deleteGroup"),


]