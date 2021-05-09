from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from  . import  views

urlpatterns = [
       path('', views.home, name='home'),
       path('odi/', views.odi_home, name='odi_home'),
       path('odi/odi_predict/', views.odi_predict, name='odi_predict'),
       path('t20/', views.t20_home, name='t20_home'),
       path('t20/t20_predict/', views.t20_predict, name='t20_predict'),
       path('ipl/', views.ipl_home, name='ipl_home'),
       path('ipl/ipl_predict/', views.ipl_predict, name='ipl_predict'),
       
]

