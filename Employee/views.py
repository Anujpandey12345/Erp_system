from django.shortcuts import render
from Employee.models import Employee, Meeting
from Employee.forms import EmployeeForm, MeetingForm
from CodingIndiaErp.forms import UserCreationForm
# Create your views here.
def AddEmployee(request):
    form = EmployeeForm()
    form2 = UserCreationForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form2 = UserCreationForm(request.POST)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            print("Form Saved !")
        else:
            print("form error", form.errors)
            print("form2 error", form2.errors)
    context = {'form': form}
    return render(request, 'Employee/addEmployee.html', context)



def AddMeeting(request):
    members = Employee.objects.all()
    form = MeetingForm()
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved Of Meeting")
        else:
            print("Form error : ", form.errors)
    context = {'members': members}
    return render(request, 'Employee/addmeeting.html', context)



# View the Staff Details 

def ShowMeetingDetails(request):
    data = Meeting.objects.all() # ojects.all() means all the objects which is inside the class
    print("Data: ", data)
    context = {'data' : data}
    return render(request, 'Employee/Showmeetingdetails.html', context)