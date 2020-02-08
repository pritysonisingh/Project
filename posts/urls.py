from django.contrib import admin
from django.urls import path

from . import views
from posts.views import PostListView,PostDetailView

app_name = 'posts'
urlpatterns=[
    path('new/',views.post, name= 'post_new'),
    path('post_list/',PostListView.as_view(), name='post_list'),
    path('post_list/<int:pk>',PostDetailView.as_view(), name='post_detail'),

]