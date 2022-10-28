from django.urls import include, re_path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

re_path(r'^$',views.employees,name='employees'),
re_path(r'^employee/(?P<query>\w+)/$',views.employeedetail,name='employeedetail'),
re_path(r'^department/(?P<query>\w+)/$',views.departmentdetail,name='departmentdetail'),
re_path(r'^project/(?P<query>\w+)/$',views.projectdetail,name='projectdetail'),



    ]