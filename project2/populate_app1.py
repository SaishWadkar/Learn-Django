import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project2.settings')

import django
django.setup()

from app1.models import Employee,EmployeeDetails
from faker import Faker

fakegen = Faker()

# print(Employee.objects.all())


def add_employee():
    emp = Employee.objects.get_or_create(name=fakegen.name())[0]
    emp.save()
    return emp

def add_employee_details():
    emp_name = add_employee()
    address = fakegen.address()
    dt = fakegen.date()

    emp_detail = EmployeeDetails.objects.get_or_create(names=emp_name,place=address,date_of_joining=dt)[0]
    print(emp_detail)

if __name__=="__main__":
    print("Hello")
    add_employee_details()
    #print(Employee.objects.all())
