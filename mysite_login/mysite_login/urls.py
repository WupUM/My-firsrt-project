
from django.contrib import admin
from django.urls import path, include
from login import views
from login.views import *
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    re_path('detail/(\d)+/', views.detail),
    path('test/<int:nid>/', views.test),
    path('create/', views.create),
    path('match/<int:nid>/', views.match),
    path('love/<int:did>/<int:rid>/', views.love),


]
