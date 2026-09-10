from django.db import models
from datetime import date

# Create your models here.
class Employee_Management_System(models.Model):
    Emp_Id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=45)
    City=models.CharField(max_length=45)
    Salary=models.IntegerField()
    Date=models.DateField(default=date.today)
    def __str__(self):
        return self.Name
    class Meta:
        managed=False
        db_table='employee_details'
        
