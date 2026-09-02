from django.db import models

# Create your models here.
class Courses(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=1000)
    Mentor=models.CharField(max_length=50)
    def __str__(self):
            return self.Name
    
class Students_Details(models.Model):
    Name=models.CharField(max_length=50)
    Class=models.CharField(max_length=50)
    Course=models.CharField(max_length=100)
    Mentor=models.CharField(max_length=100)
    MobileNo=models.CharField(max_length=15)
    def __str__(self):
        return self.Name
