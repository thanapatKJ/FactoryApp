from django.urls import path
from . import views

app_name='manager'
urlpatterns = [
    # กลุ่มงาน
    path('', views.index, name="index"),
    # แผนงาน
    path('plan/', views.plan, name="plan"),
]