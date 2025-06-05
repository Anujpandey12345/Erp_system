from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    task = models.TextField(max_length=300)
    staff = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task