
from django.forms.models import ModelForm
from database.models import Branchs, WorkGroups, WorkPlans
from database.models import Users

class WorkPlanForm(ModelForm):
    class Meta:
        model=WorkPlans
        fields= '__all__'
