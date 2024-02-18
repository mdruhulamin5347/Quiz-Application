from django.urls import path
from .views import *
urlpatterns = [
    path('contact/', CONTACT, name='contact'),
    path('login/',LOGINPAGE, name='login'),
    path('logout/',LOGOUTPAGE, name='logout'),
    path('signup/',SINGUP, name='signup')
]
