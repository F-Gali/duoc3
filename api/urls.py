from django.urls import path
from .views import *

urlpatterns = [
    path('articulos/', articles_list),
    path('articulos/<int:article_id>', article_detail),
]