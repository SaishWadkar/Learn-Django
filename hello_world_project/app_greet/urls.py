from django.urls import path
from app_greet import views

urlpatterns = [
    path('',views.index,name='index'),
    path('app_greet/',views.index_new,name="index_new"),
    path('/admin',views.index_new,name="index")
]
