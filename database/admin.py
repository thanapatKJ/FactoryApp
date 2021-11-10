from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class WorkGroupInline(admin.TabularInline):
    model = WorkGroup.manager.through

admin.site.register(User)
admin.site.register(WorkPlan)
admin.site.register(UserHistory)

@admin.register(WorkGroup)
class WorkGroupAdmin(admin.ModelAdmin):
    inlines = (WorkGroupInline,)
    
# admin.site.register(WorkGroup,WorkGroupInline)
