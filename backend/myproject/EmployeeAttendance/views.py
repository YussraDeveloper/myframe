from django.shortcuts import render, redirect
from .models import Employee, Attendance

# Create your views here.
from datetime import date

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
