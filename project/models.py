from django.db import models
from django.utils import timezone

# Create your models here.

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    subcat = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name



class projectModel(models.Model):
    name = models.CharField(max_length=100)
    projectdate = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True)
    desp = models.TextField(default="")
    image = models.ImageField(blank=True, null=True)
    finishdatetime = models.DateTimeField(auto_now_add=True)
    payment = models.IntegerField()
    paymentreceive = models.FloatField()


    def __self__(self):
        return self.name