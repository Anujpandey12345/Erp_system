# views.py
from django.shortcuts import render, redirect
from CodingIndiaErp.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# For email
from django.core.mail import send_mail
import random
from CodingIndiaErp.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# @csrf_exempt
# def verifyOTP(request):
#     if request.method == "POST":
#         print("Incoming POST data:", request.POST)
#         userotp = request.POST.get('otp')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1 == password2:
#             form = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
#             form.save()

#         print("OTP: ", userotp)
#     return JsonResponse({'data':'Hello'}, status=200)
@csrf_exempt
def verifyOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if userotp == session_otp:
            user_data = request.session.get('pending_user')
            if user_data:
                if user_data['password1'] == user_data['password2']:
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name'],
                        password=user_data['password1']
                    )
                    return JsonResponse({'message': 'User created successfully!'}, status=200)
                else:
                    return JsonResponse({'error': 'Passwords do not match'}, status=400)
            else:
                return JsonResponse({'error': 'User session expired'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid OTP'}, status=400)



def SignUpView(request):
    form = CreateUserForm()
    if request.method == "POST":

        
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')  

        form = CreateUserForm(request.POST)


        if form.is_valid():
            otp = random.randint(100000,999999)
            form.save()
            print("Form Saved")
            send_mail(subject="User Data",message=f"Verify your Mail by opt /n{otp}",from_email=EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
            messages.success(request, "User Saved Successfully !!")
            return render(request,'verify.html',{'otp':otp, 'first_name':first_name, 'last_name':last_name, 'username':username, 'password1':password1, 'password2':password2})
            # return redirect('login')  # Redirect to login or another page after successful registration
        else:
            print("Form Error:", form.errors)
            messages.error(request, form.errors)
    context = {"form": form}
    return render(request, 'signup.html', context)


# For login
@csrf_exempt
def verifyLoginOTP(request):
    if request.method == "POST":
        # print("Incoming POST data:", request.POST)
        userotp = request.POST.get('otp')
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("LOGIN DONE!!")

        print("OTP: ", userotp)
    return JsonResponse({'data':'Hello'}, status=200)
def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = User.objects.get(username=username).email
        
        print("username:", username)
        print("password:",password)
        print("email:", email)

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
            
        #     login(request, user)
        #     print("Login saved")
        #     messages.success(request, "Login Successfully !!")

        #     return redirect("/")
        # else:
        #     print("Some Error")
        otp = random.randint(100000,999999)
        send_mail(subject="User Data",message=f"Verify your LoginMail by opt : {otp}",from_email=EMAIL_HOST_USER,recipient_list=[email],fail_silently=False)
        messages.success(request, "User Saved Successfully !!")
        return render(request,'verifyloginotp.html',{'otp':otp, 'username':username, 'password':password})
        #     messages.error(request, "Invalid Details !!")

        


        
    context = {}
    return render(request, 'login.html', context)


def LogOut(request):
    logout(request)
    print("LogOut Successfully")
    messages.success(request, "Logout Successfully !!")


    return redirect("loginview")