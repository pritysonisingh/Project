from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views
from account.views import IndexView

app_name = 'account'

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('signup/', views.signup, name= 'signup'),
    path('profile/',views.view_profile, name='profile'),
    path('profile/<int:pk>/',views.view_profile, name='user-profile'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
    path('connect/<operation>/<int:pk>',views.change_friends, name='change_friends'),
    # url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    path('change_password/', views.change_password, name= 'change_password'),

]