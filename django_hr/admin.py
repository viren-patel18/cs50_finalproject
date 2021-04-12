from django.contrib import admin
from .models import User, Employee, Department, Position, LeaveRequest, Announcement, Objective, CheckIn

# Register your models here.
admin.site.unregister(User)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(LeaveRequest)
admin.site.register(Announcement)
admin.site.register(Objective)
admin.site.register(CheckIn)