from django.urls import path
from .views import *

urlpatterns = [
    path('articulos/', articles_list),
    path('articulos/<int:article_id>', article_detail),
    path('companias/',company_list),
    path('companias/<int:company_id>', company_detail),
    path('mensajes/', messages_list),
    path('mensajes/<int:message_id>', message_detail),
    path('comentarios/', comments_list),
    path('comentarios/<int:comment_id>', comment_detail),
]