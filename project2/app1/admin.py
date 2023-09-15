from django.contrib import admin

# Register your models here.
from app1.models import Employee,EmployeeDetails

admin.site.register(Employee)
admin.site.register(EmployeeDetails)
