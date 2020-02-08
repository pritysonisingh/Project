from django.contrib import admin
from django.urls import path

from . import views
app_name = 'account'
urlpatterns = [
    path('',views.index, name='index'),
    path('signup/', views.signup, name= 'signup'),
    path('profile/',views.view_profile, name='profile'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name= 'change_password'),

]