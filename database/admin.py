from django.contrib import admin
from .models import User, WorkGroup, WorkPlan, UserHistory
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(WorkPlan)
admin.site.register(UserHistory)
admin.site.register(WorkGroup)
