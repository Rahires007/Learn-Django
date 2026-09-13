from django.db import models

# Create your models here.
class Task_Manager(models.Model):
    Task=models.CharField(max_length=1000)
    Status=models.CharField(default="Pending")
    Added_Date=models.DateTimeField(auto_now_add=True)
    Updated_Date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Task