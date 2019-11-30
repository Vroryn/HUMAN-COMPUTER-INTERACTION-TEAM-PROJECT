from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Customers_List

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class Profile_Edit_Form(forms.ModelForm):

    
    middle_name = forms.CharField(required=False)
    zipcode = forms.IntegerField(required=True)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = Customers_List
        fields = [
           'first_name',
           'middle_name',
           'last_name',
           'address',
           'city',
           'state',
           'zipcode',
           'phone_number',
           
        ]
