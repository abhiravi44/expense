from . import views
from django.conf.urls import url
from django.contrib import admin



urlpatterns=[
    url(r'^index/',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^saverec/',views.saverec,name='saverec'),
    url(r'^getreportbycategory',views.getreportbycategory,name='getreportbycategory'),
    url(r'^allrecord',views.allrecord,name='allrecord'),
    url(r'^userlogin',views.userlogin,name='userlogin'),
    url(r'^getreportbydate',views.getreportbydate,name='getreportbydate'),
    url(r'^register1',views.register1,name='register1'),
    url(r'^login1',views.login1,name='login1'),
    url(r'^logout1',views.logout1,name='logout1'),


]