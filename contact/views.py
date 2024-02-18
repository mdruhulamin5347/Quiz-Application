
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def CONTACT(request):
    return render(request,'contact.html')



def LOGINPAGE(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'succesfully logined')
                return redirect('/quizzes/')
    else:
        form=AuthenticationForm()

    return render(request,'login.html', {'form':form})

def LOGOUTPAGE(request):
    logout(request)
    messages.success(request, 'successfully logout the page')
    return redirect('/quizzes/')

from .forms import UserCreateForm
def SINGUP(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/contact/login/')
           
        
    else:
        form=UserCreateForm()
    return render(request, 'signup.html', {'form':form})

