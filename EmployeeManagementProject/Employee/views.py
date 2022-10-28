from django.shortcuts import render


from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import (Department,
                     Employee,
                    Project,
                    WorkOn
                     )

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request,'index.html',{})

    # if(request.method=='POST'):
    #     username =  request.POST['username']
    #     password =  request.POST['password']
    #     user = authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         username = request.user.username
    #         authorusername = str(request.user.username)
    #
    #     if request.user.is_authenticated:
    #         authorusername = str(request.user.username)
    #         employeecount = Employee.objects.all().count()
    #         departmetncount = Department.objects.all().count()
    #         projectcount = Project.objects.all().count()
    #
    #         return render(request,'index.html',
    #                                   {'authorusername':authorusername,
    #                                    'employeecount':employeecount,
    #                                    'departmetncount':departmetncount,
    #                                    'projectcount':projectcount
    #                                    })
    #     return redirect('/admin/login')
    # return redirect('/admin/login')


@login_required
def employees(request):

    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        employees = Employee.objects.all()
        project_list = []
        len_e = len(employees)
        for it in range(len(employees)):
            temp1  = employees[it].project.all()
            for item3 in temp1:
                project_list.append((item3.name,employees[it].number))
        return render(request,'employees.html',context=
                                  {'authorusername':authorusername,
                                   'employees':employees,
                                   'len':len_e,'project_list':project_list
                                   }
                                  )
@login_required
def employeedetail(request,query):
    if request.user.is_authenticated:
        authorusername  = str(request.user.username)
        employee = Employee.objects.filter(number=query).get()
        project_list = employee.project.all()
        return render(request,'employeedetail.html',
                                  {'authorusername': authorusername,
                                   'employee': employee,
                                    'project_list': project_list
                                   }

                                  )

@login_required
def departmentdetail(request,query):
    if request.user.is_authenticated:
        authorusername = str(request.user.username)
        department  = Department.objects.filter(number=query).get()
        employee_count= Employee.objects.filter(department__pk=query).count()
        return render(request,'departmentdetail.html',
                                  {'authorusername': authorusername,
                                   'department': department,
                                   'employee_count': employee_count
                                   }
                                  )

@login_required
def projectdetail(request,query):
    if request.user.is_authenticated:
        authorusername = str(request.user.username)
        project = Project.objects.filter(number=query).get()
        employee_count = Employee.objects.filter(department__pk=query).count()
        return render(request,'projectdetail.html',
                                  {'authorusername': authorusername,
                                   'project': project,
                                   'employee_count': employee_count
                                   }
                                  )

