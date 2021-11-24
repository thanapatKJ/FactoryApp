from django.db import models


from django.contrib.auth.models import AbstractUser, Group
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey, OneToOneField



class Branchs(models.Model):
    name = models.CharField(max_length=30,primary_key=True)

    class Meta:
        ordering=["name"]
        verbose_name = "Branch"

    def __str__(self):
        return str(self.name)
    
class Users(AbstractUser):
    id_card = models.CharField(null=False,blank=False,max_length=13)
    ROLES = (
        ('ผู้ดูแล','ผู้ดูแล'),
        ('หัวหน้างาน','หัวหน้างาน'),
        ('พนักงาน','พนักงาน'),
    )
    roles = models.CharField(max_length=30,choices=ROLES,null=False)
    class Meta:
        ordering = ["roles"]
        verbose_name = "User"

    def __str__(self): 
        return str(self.first_name) + " " + str(self.last_name) +" - "+str(self.roles)

class WorkBranchs(models.Model):
    branch = models.ForeignKey(Branchs ,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    class Meta:
        ordering= ["branch"]
        verbose_name = "WorkBranch"

    def __str__(self):
        return str(self.branch.name)+ " - "+str(self.user.first_name)+" "+str(self.user.last_name)

class WorkGroups(models.Model):
    branch = models.ForeignKey(Branchs,on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50,unique=True,)

    class Meta:
        verbose_name = "WorkGroup"

    def __str__(self):
        return str(self.group_name)

class ManageBranchs(models.Model):
    manager = OneToOneField(Users,on_delete=models.CASCADE)
    branch = OneToOneField(Branchs,on_delete=models.CASCADE)
    class Meta:
        ordering = ["branch"]
        verbose_name = "ManageBranch"

    def __str__(self):
        return str(self.branch)+ " - " +str(self.manager.first_name)+" "+str(self.manager.last_name)

class WorkPlans(models.Model):
    group_name = models.ForeignKey(WorkGroups,on_delete=models.CASCADE)
    datetime_start = models.DateTimeField(null=False,blank=False)
    datetime_end = models.DateTimeField(null=False,blank=False)
    limit_ot_hour = models.FloatField(default=0.0)
    class Meta:
        verbose_name = "WorkPlan"
        ordering = ["datetime_start"]
    def __str__(self):
        return str(self.group_name.group_name)+": ("+str(self.datetime_start)+") - ("+str(self.datetime_end)+")"

class UserHistories(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    plan = models.ForeignKey(WorkPlans,on_delete=models.CASCADE)
    datetime_checkin = models.DateTimeField(null=True,blank=True)
    datetime_checkout = models.DateTimeField(null=True,blank=True)
    ot_hour = models.FloatField(default=0.0)
    custom_ot = models.BooleanField(default=False)
    class Meta:
        ordering = ["-plan__datetime_start"]
        verbose_name = "UserHistorie"

    def __str__(self):
        return str(self.user.first_name)+" "+str(self.user.last_name) + " - "+str(self.plan.group_name.group_name)+" ["+str(self.plan.datetime_start)+"  -  "+str(self.plan.datetime_start)+"]"  

class Machines(models.Model):
    branch = models.ForeignKey(Branchs, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=30)
    choice = (
        ('ปกติ','ปกติ'),
        ('ส่งซ่อม','ส่งซ่อม'),
        ('เสียหาย','เสียหาย'),
    )
    status = models.CharField(max_length=30,choices=choice,null=False)
    class Meta:
        verbose_name = "Machine"

# class MachineUsages(models.Model):
#     user = ForeignKey(Users,on_delete=models.CASCADE)
#     machines = OneToOneField()