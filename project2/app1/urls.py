
from django.urls import path
from app1 import views

urlpatterns = [
    path('help/',views.help,name='help'),
    path('',views.index,name='index')
]
