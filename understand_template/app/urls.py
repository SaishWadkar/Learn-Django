from django.contrib import admin
from django.urls import path
from app import views

# termplate tagging
app_name = "app"

urlpatterns = [
    path('other/',views.other , name='other'),
    path('relative/',views.relative , name='relative'),
]
