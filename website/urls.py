from os import path

from django.shortcuts import render
from django.urls import path
from .import views
from django.http import HttpResponse


app_name = "website"


urlpatterns = [
    path('', views.base_page_view),
    path('home', views.home_page_view),
    path('mtb', views.mtb_page_view),
    path('road', views.road_page_view),
    path('bmx', views.bmx_page_view),
    path('signup', views.signup_page_view, name='signup'),
    path('login', views.login_page_view),
    path('logout', views.logout_page_view, name='logout'),
    path('myinfo', views.myinfo_page_view),
    path('create-comment', views.create_comment_page_view, name='create_comment'),
    path('comment-list', views.comments_list_page_view, name='comment-list'),


]



