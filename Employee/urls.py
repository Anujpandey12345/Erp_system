from django.urls import path, include
from Employee import views
urlpatterns = [
    path('', views.AddEmployee, name='addEmployee'),
    path('AddMeeting/', views.AddMeeting, name='addmeeting'),
    path('ShowMeetingDetails/', views.ShowMeetingDetails, name='showmeetingdetails')



]