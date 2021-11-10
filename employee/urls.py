from django.urls import path
from . import views

app_name='employee'
urlpatterns = [
    path('', views.index, name="index"),
    path('history/', views.history, name="history"),
    path('plan/', views.plan, name="plan"),
    path('info/', views.info, name="info"),
    path('history/<str:id>', views.historyInfo, name="historyInfo"),
    path('plan/', views.plan, name="plan"),
    path('plan/<str:id>', views.planInfo, name="planInfo"),


]