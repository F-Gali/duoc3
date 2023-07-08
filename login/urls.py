from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home-login'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('success', success, name='success'),    
]