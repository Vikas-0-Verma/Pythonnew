from django.contrib import admin
from django.contrib.auth.models import User
from .models import (Department,
                     Employee,
                    Project,
                    WorkOn
                     )
# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(WorkOn)

