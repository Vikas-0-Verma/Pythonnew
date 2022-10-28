from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Department(models.Model):
    name = models.CharField(verbose_name="Name",max_length = 1000,blank=True,null=True)
    number = models.CharField(verbose_name="Number",max_length = 1000,blank=True,primary_key=True)

    def __str__(self):
        return str(self.name)+" - "+str(self.number)

class Project(models.Model):
    name = models.CharField(verbose_name="Name",max_length=1000,blank=True,null=True)
    number = models.CharField(verbose_name="Number", max_length=1000, blank=True, primary_key=True)

    def __str__(self):
        return str(self.name)+" - "+str(self.number)

    def project_ids(self):
        return "project_"+str(self.id)

class Employee(models.Model):
    name = models.CharField(verbose_name="Name", max_length=1000, blank=True, null=True)
    number = models.CharField(verbose_name="Number", max_length=1000, blank=True, primary_key=True)
    salary = models.CharField(verbose_name="Salary", max_length=1000, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True,related_name='departmentname',default="null",on_delete=models.CASCADE)
    project=  models.ManyToManyField(Project,through='WorkOn')


    def __str__(self):
        return str(self.name) + " - " + str(self.number)+" - "+str(self.department.number)

class WorkOn(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.employee.name)+" - " +str(self.project.name)