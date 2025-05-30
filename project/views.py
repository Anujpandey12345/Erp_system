from django.shortcuts import render
from project.models import projectModel
from project.forms import createForm, createForm
# Create your views here.

# This is Function Based project
def create_project(request):
    form = projectModel
    if request.method == 'POST':
        form = createForm(request.POST)

        if form.is_valid():
            form.save()
            print("Right")
        else:
            print("Not right", form.errors)
    context = {'form' : form}  #For display the backend data into frontend
    return render(request, 'project/create_project.html', context)



def showProjectData(request):
    data = projectModel.objects.all() # ojects.all() means all the objects which is inside the class(project model)
    print("Data: ", data)
    context = {'data': data} # This is help us to show our data on the front end from the backend.
    return render(request, 'project/showProjectData.html', context)