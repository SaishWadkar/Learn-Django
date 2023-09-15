from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name

class EmployeeDetails(models.Model):
    names = models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    place = models.CharField(max_length=264)
    date_of_joining = models.DateField()

    def __str__(self):
        return str(self.names)+ " from " + self.place + " had joined on "+str(self.date_of_joining)
