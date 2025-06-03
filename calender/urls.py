from django.urls import path, register_converter
from . import views
urlpatterns = [
    path('', views.CalenderRedirect),  # optional homepage
    path('calender/', views.CalenderRedirect, name='calender_default'),  # <== this one fixes your issue
    path('calender/<int:year>/<str:month>/', views.Calender, name='calender'),
]