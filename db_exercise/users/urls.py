from django.contrib import admin
from django.urls import path
from django.urls import include
from users import views

urlpatterns = [
    path('', views.index , name='index'),
    path('users/', views.users_list , name='userlist'),
    path('signup/', views.new_user_view , name='from'),
]
