from django.shortcuts import redirect, render
from datetime import datetime
import calendar

def CalenderRedirect(request):
    now = datetime.now()
    return redirect('calender', year=now.year, month=now.strftime('%B'))

def Calender(request, year, month):
    # Capitalize the month name
    month = month.capitalize()
    
    # Convert month from name to number
    month_names = list(calendar.month_name)
    month_number = month_names.index(month)
    month_number = int(month_number)
    
    # Create a calendar
    cal = calendar.HTMLCalendar().formatmonth(
        year,
        month_number
    )
    
    # Calculate previous month
    if month_number == 1:
        prev_month_number = 12
        prev_year = year - 1
    else:
        prev_month_number = month_number - 1
        prev_year = year
    
    prev_month = calendar.month_name[prev_month_number].lower()
    
    # Calculate next month
    if month_number == 12:
        next_month_number = 1
        next_year = year + 1
    else:
        next_month_number = month_number + 1
        next_year = year
    
    next_month = calendar.month_name[next_month_number].lower()
    
    # Get current year and time
    now = datetime.now()
    current_year = now.year
    current_time = now.strftime("%B %d, %Y at %I:%M %p")
    
    context = {
        'cal': cal,
        'year': year,
        'month': month,
        'month_number': month_number,
        'current_year': current_year,
        'time': current_time,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }
    
    return render(request, 'calender/event.html', context)