from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    path('commentaire/<int:id>',views.creer_comment,name='creer_comment'),
    url(r'^(?P<slug>.+)$', views.lire_article, name='blog_lire'),
]

