from django.contrib import admin

# Register your models here.
# Admin is use for that we show the both table to admin that check thats tables
from Employee.models import Dept, Employee

admin.site.register(Dept)
admin.site.register(Employee)

