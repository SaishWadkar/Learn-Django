from django.shortcuts import render
from django.http import HttpResponse

# importing models
from app1.models import Employee,EmployeeDetails


# Create your views here.

def view1(request):
    return HttpResponse("<h1>Hello App 1 </h1>")

def index(request):
    emp = EmployeeDetails.objects.order_by('date_of_joining')
    emp_dict = {'employee':emp}
    return render(request,'app1/index.html',context=emp_dict)

def help(request):
    dict = {'insert':'hey there . im using python'}
    return render(request,'app1/help.html',context=dict)
