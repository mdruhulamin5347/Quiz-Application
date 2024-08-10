from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactModel

class UserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
    
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields = '__all__'
