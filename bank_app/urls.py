
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login_user/',views.login_user,name='login_user'),
    path('register/',views.register,name='register'),
    path('newpg/',views.newpg,name='newpg'),
    path('bankform/',views.bankform,name='bankform'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('success/',views.success,name='success'),
]