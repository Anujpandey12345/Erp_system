from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.TaskPage, name='taskpage'),
    path('create/', views.Create_todo, name='create_todo'),

]