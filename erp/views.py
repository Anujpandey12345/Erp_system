from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.signals import request_finished
from django.dispatch import receiver

# # Create your views here.


def Index(request):
    context = {} # Context is use for when we want the backend data to show in the Frontend means we use the context for showing the data.
    return render(request, 'dashboard.html', context)

# For the contact page
def contact(request):
    return render(request, 'contact.html')


def showStaff(request):
    data = User.objects.all() # use for data save 

    context = {'data' :  data}
    return render(request, 'showStaff.html', context)

def viewStaffData(request, id):
    data = User.objects.get(id=id) # use for data save 

    context = {'data' :  data}
    return render(request, 'viewStaffData.html', context)