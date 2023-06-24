from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    # path('compania/<int:id>/', compania, name='compania')
]