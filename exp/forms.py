from . models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class StaffForm(UserCreationForm):
    class Meta:
        model=Users
        fields=['username','first_name','last_name','email','password1','password2']




class ListForm(forms.ModelForm):
    category=(("user","User"),("admin","Admin"))
    Category=forms.MultipleChoiceField(choices=category)
    class Meta:
        model=user_model
        fields=[
            'Name','Image','Username','Password','Category'
        ]
        # widgets={
        #     'Name':TextInput(attrs={'class':'color'}),
        #     'Username':TextInput(attrs={'class':'color' }),
        #     'Password':TextInput(attrs={'class':'color' }),
        #     'Category':TextInput(attrs={'class':'color' })
        # }

class RecordForm(forms.ModelForm):
    class Meta:
        model=record
        fields=[
            'Description','Category','Amount'
        ]
        widgets={
            
        }