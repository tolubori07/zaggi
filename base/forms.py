from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User,Address


class Myusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class userform(ModelForm):
    class Meta:
       model = User
       fields = ['name','username', 'email']

class addressform(ModelForm):
    class Meta:
        model = Address
        fields = ['house_number','street_name','county','city']