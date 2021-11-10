from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey, OneToOneField


class User(AbstractUser):
    id_card = models.CharField(null=False,blank=False,max_length=13)
    ROLES = (
        ('หัวหน้างาน','หัวหน้างาน'),
        ('พนักงาน','พนักงาน'),
        ('ผู้ดูแล','ผู้ดูแล'),
    )
    roles = models.CharField(max_length=30,choices=ROLES,null=False)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) +" - "+str(self.roles)

class WorkGroup(models.Model):
    work_group = models.CharField(max_length=50,primary_key=True)
    manager = models.ManyToManyField(User)
    def __str__(self):
        return str(self.work_group)+" : "+ str(self.manager)

class WorkPlan(models.Model):
    work_group = models.ForeignKey(WorkGroup,on_delete=models.CASCADE)
    datetime = models.CharField(max_length=80,primary_key=True)
    datetime_start = models.DateTimeField(null=False,blank=False)
    datetime_end = models.DateTimeField(null=False,blank=False)
    limit_ot_hour = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.work_group.work_group)+": ("+str(self.datetime_start)+") - ("+str(self.datetime_end)+")"

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(WorkPlan,on_delete=models.CASCADE)
    datetime_checkin = models.DateTimeField(null=True,blank=True)
    datetime_checkout = models.DateTimeField(null=True,blank=True)
    ot_hour = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.user.first_name) +" "+str(self.user.last_name) + " - "+str(self.plan.work_group.work_group)+" "+str(self.plan.datetime)
