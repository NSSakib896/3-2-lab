from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('alluser/', views.all_user, name='alluser'),
    path('userlogin/details/<int:id>', views.details, name='details')
]