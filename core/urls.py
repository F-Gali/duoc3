from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('articles/', articles, name='articles'),
    path('articles/compania/<compania>', articles_by_company, name='articles-company'),
    path('articles/article/<id_articulo>', articulo_completo, name='article-complete'),
    # path('compania/<int:id>/', compania, name='compania')
]