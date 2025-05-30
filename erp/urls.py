from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('showstaff/', views.showStaff, name='showStaff'),
    path('showstaffData/<int:id>/', views.viewStaffData, name='viewStaffData'),

]