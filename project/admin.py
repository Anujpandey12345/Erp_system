from django.contrib import admin
from project.models import projectModel, ProjectCategory
# Register your models here.

admin.site.register(projectModel)
admin.site.register(ProjectCategory)