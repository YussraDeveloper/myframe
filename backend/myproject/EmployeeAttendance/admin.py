from django.contrib import admin
from .models import Employee, Attendance

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'position', 'department')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('attendance_id', 'employee', 'date', 'status')
    list_filter = ('date', 'status')
