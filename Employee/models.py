from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25)
    dob = models.DateField()
    department = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

