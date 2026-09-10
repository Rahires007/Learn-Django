from django.db import models

# Create your models here.
class Students_Database(models.Model):
    Name=models.CharField(max_length=100)
    Class=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    def __str__(self):
        return self.Name
