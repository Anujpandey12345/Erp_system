# admin.py
from django.contrib import admin
from .models import Todo  # Make sure this import is correct

admin.site.register(Todo)
