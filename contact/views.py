
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def CONTACT(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = "Quiz Project Contact Form Submission"
            message = f"Message from {form.cleaned_data['name']} \n ({form.cleaned_data['email']}):\n\n{form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']
            recipient_list = ['myprojects.helpservice@gmail.com']
            send_mail(subject, message, from_email, recipient_list)
            form = ContactForm()
            messages.success(request, "Your message has been sent successfully!")
        else:    
            messages.error(request, "There was an error in your submission. Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



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
            return redirect('login')
    else:
        form=UserCreateForm()
    return render(request, 'signup.html', {'form':form})


from home.models import QuizScore
def PROFILE(request):
    user = request.user
    quiz = QuizScore.objects.filter(user=user)
    return render(request,'profile.html',{'quiz':quiz})

