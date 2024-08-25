from django.urls import path
from .views import *
urlpatterns = [
    path('contact/', CONTACT, name='contact'),
    path('login/',LOGINPAGE, name='login'),
    path('logout/',LOGOUTPAGE, name='logout'),
    path('signup/',SINGUP, name='signup'),
    path('Profile/',PROFILE,name='profile'),
    path('change/',CHANGE, name='change_password'),
    path('password-reset/',PasswordReset, name='password_reset'),  
]
