from django.contrib import admin
from django.urls import path

from . import views
from account.views import IndexView

app_name = 'account'
urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('signup/', views.signup, name= 'signup'),
    path('profile/',views.view_profile, name='profile'),
    path('profile/<int:pk>/',views.view_profile, name='user-profile'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
    path('connect/<operation>/<int:pk>',views.add_friend, name='change-friend'),
    path('change_password/', views.change_password, name= 'change_password'),

]