from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=100)          # Name of the employee
    position = models.CharField(max_length=100)      # Position of the employee
    department = models.CharField(max_length=100)    # Department of the employee

    def __str__(self):
        return f"{self.name} ({self.position})"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Link to Employee table
    date = models.DateField()                            # Date of attendance
    status = models.CharField(max_length=10, choices=[  # Status of attendance
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ])

    def __str__(self):
        return f"Attendance for {self.employee.name} on {self.date}: {self.status}"
