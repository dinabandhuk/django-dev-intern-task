from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Address = models.CharField(max_length=300)
    Grade = models.CharField(max_length=1)
    Major = models.CharField(max_length=100)
    