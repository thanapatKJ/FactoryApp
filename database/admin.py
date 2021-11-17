from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin

# class WorkGroupInline(admin.TabularInline):
#     model = WorkGroups.manager.through

admin.site.register(Users)
admin.site.register(WorkPlans)
admin.site.register(UserHistories)
admin.site.register(Branchs)
admin.site.register(WorkBranchs)
admin.site.register(WorkGroups)
admin.site.register(ManageBranchs)
admin.site.register(Machines)

# @admin.register(WorkGroups)
# class WorkGroupAdmin(admin.ModelAdmin):
#     inlines = (WorkGroupInline,)
    
# admin.site.register(Users,UserAdmin)
