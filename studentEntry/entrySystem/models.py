from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    address = models.TextField()
    grade = models.CharField(max_length=1)
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name