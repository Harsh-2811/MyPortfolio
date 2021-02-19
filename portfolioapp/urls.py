from django.urls import path
from .views import index,sendemail,projectpage

urlpatterns = [
    path("",index,name='index'),
    path("sendemail/",sendemail,name='index'),
    path("project/<slug>",projectpage,name='index'),

]