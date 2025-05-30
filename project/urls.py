from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.create_project, name='create_project'),
    path('showProjectData/', views.showProjectData, name='show_project_data'),

]