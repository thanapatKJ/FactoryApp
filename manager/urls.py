from django.urls import path
from . import views

app_name='manager'
urlpatterns = [
    # กลุ่มงาน
    path('', views.index, name="index"),
    path('group/<str:gid>', views.group, name="group"),

    # แผนงาน
    path('plan/', views.Allplan, name="Allplan"),
    path('plan/<str:pid>/deletePlan', views.deletePlan, name="deletePlan"),
    path('plan/addPlan', views.addPlan, name="addPlan"),
    path('plan/<str:pid>/deletePlan', views.deletePlan, name="deletePlan"),
    path('plan/<str:pid>/', views.plan, name="plan"),
    path('plan/<str:hid>/removeUser/<str:uid>', views.removeUser, name="removeUser"),
    # ข้อมูล
    path('info/', views.info, name="info"),

]