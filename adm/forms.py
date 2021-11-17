
from django.forms.models import ModelForm
from database.models import WorkGroups
from django.contrib.auth.forms import UserCreationForm
from database.models import Users

class UserForm(UserCreationForm):
    class Meta:
        model=Users
        fields=('username','first_name','last_name','email','password1','password2','id_card','roles')

class WorkGroupPlan(ModelForm):
    class Meta:
        model=WorkGroups
        # fields= ('manager',)
        fields= '__all__'

# class AddManagerForm(ModelForm):
#     class Meta:
#         model=WorkGroups
#         fields= ('manager',)
        # fields= '__all__'
    # def __init__(self, *args,**kwargs):
    #     super (AddManagerForm,self ).__init__(*args,**kwargs)
    #     self.fields['manager'].queryset = WorkGroup.objects.filter(manager__roles='หัวหน้างาน')