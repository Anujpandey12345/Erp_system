from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def TaskPage(request):
    today = timezone.now().date()
    sometasks = Todo.objects.filter(date=today)  # Only today's tasks
    return render(request, 'task/show.html', {'sometasks': sometasks})


from django.utils import timezone
from .models import Todo

def Create_todo(request):
    if request.method == "POST":
        staff = request.POST.get("staff")
        task = request.POST.get("task")
        Todo.objects.create(
            staff=staff,
            task=task,
            date=timezone.now().date()  # ✅ Fix: only save the date part
        )
    return render(request, 'task/task1.html')
