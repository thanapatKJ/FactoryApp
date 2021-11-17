
from django.contrib.auth.forms import UserCreationForm
from database.models import Users

class UserForm(UserCreationForm):
    class Meta:
        model=Users
        fields=('username','first_name','last_name','email','password1','password2','id_card','roles')
